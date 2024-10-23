# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from .tokens import account_activation_token
from .models import Todo, Note
from .forms import SignUpForm, TodoForm, NoteForm
from django.contrib.auth.views import LogoutView, LoginView
from django.http import JsonResponse
from django.conf import settings


    
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                # Create user but don't activate yet
                user = form.save(commit=False)
                user.is_active = False  # Deactivate account till it is confirmed
                user.save()
                
                # Send activation email
                mail_subject = 'Activate your account.'
                message = render_to_string('core/acc_active_email.html', {
                    'user': user,
                    'domain': settings.APP_URL,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.content_subtype = "html"
                email.send()
                
                messages.success(request, 'Please confirm your email address to complete the registration.')
                return redirect('login')
                
            except Exception as e:
                # If an error occurs during user creation or email sending
                messages.error(request, f"An error occurred during registration: {str(e)}")
        else:
            # If the form is not valid, display the errors
            messages.error(request, "The provided data is not valid. Please correct the errors below.")
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.profile.is_verified = True
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, 'Your account has been confirmed.')
        return redirect('home')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required
def home(request):
    return render(request, 'core/home.html')


@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'core/todo_list.html', {'todos': todos})

@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'core/todo_form.html', {'form': form})

@login_required
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'core/todo_form.html', {'form': form})

@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'core/todo_confirm_delete.html', {'todo': todo})

@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'core/note_list.html', {'notes': notes})

@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'core/note_form.html', {'form': form})

@login_required
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'core/note_form.html', {'form': form})

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'core/note_confirm_delete.html', {'note': note})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html' 


class CustomLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        logout(request)
        # Return a JSON response on successful logout
        return JsonResponse({"status": "success"})

    def get(self, request, *args, **kwargs):
        # Call the post method to handle GET requests as well
        return self.post(request, *args, **kwargs)
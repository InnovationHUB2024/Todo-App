from django.test import SimpleTestCase
from django.test import TestCase
from django.urls import reverse, resolve
from core import views as core_views
from core.forms import SignUpForm ,TodoForm, NoteForm
from core.models import Todo, Note
from django.contrib.auth.models import User

# URL Tested By Gideon Olagbemiro 

# class TestUrls(SimpleTestCase):
    

#     def test_list_url_is_resolved(self):
#         url = reverse('login')
#         self.assertEqual(resolve(url).func.view_class, core_views.CustomLoginView)

#     def test_detail_url_is_resolved(self):
#         url = reverse('logout')
#         self.assertEqual(resolve(url).func.view_class, core_views.CustomLogoutView)

#     def test_create_url_is_resolved(self):
#         url = reverse('signup')
#         self.assertEqual(resolve(url).func, core_views.signup)

#     def test_update_url_is_resolved(self):
#         url = reverse('home')
#         self.assertEqual(resolve(url).func, core_views.home)

#     def test_delete_url_is_resolved(self):
#         url = reverse('todo_list', args=[1])
#         self.assertEqual(resolve(url).func, core_views.todo_list)
        
#     def test_delete_url_is_resolved(self):
#         url = reverse('todo_create', args=[1])
#         self.assertEqual(resolve(url).func, core_views.todo_create)

        
#     def test_delete_url_is_resolved(self):
#         url = reverse('todo_update', args=[1])
#         self.assertEqual(resolve(url).func, core_views.todo_update)
        
#     def test_delete_url_is_resolved(self):
#         url = reverse('todo_delete', args=[1])
#         self.assertEqual(resolve(url).func,  core_views.todo_delete)
        
#     def test_delete_url_is_resolved(self):
#         url = reverse('note_list', args=[1])
#         self.assertEqual(resolve(url).func, core_views.note_list)
        
#     def test_delete_url_is_resolved(self):
#         url = reverse('note_create', args=[1])
#         self.assertEqual(resolve(url).func, core_views.note_create)
        
#     def test_delete_url_is_resolved(self):
#         url = reverse('note_update', args=[1])
#         self.assertEqual(resolve(url).func, core_views.note_update)
        
#     def test_delete_url_is_resolved(self):
#         url = reverse('note_delete', args=[1])
#         self.assertEqual(resolve(url).func, core_views.note_delete)
    

# Form Tests By   
class TestForms(TestCase):

    def test_signup_form_valid_data(self):
        form = SignUpForm(data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
        })
        self.assertTrue(form.is_valid())

    def test_signup_form_no_data(self):
        form = SignUpForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)  # Adjust the number of required fields if necessary

    def test_todo_form_valid_data(self):
        form = TodoForm(data={
            'title': 'Test Todo',
            'description': 'Test Description',
            'completed': False,
        })
        self.assertTrue(form.is_valid())

    def test_todo_form_no_data(self):
        form = TodoForm(data={})
        self.assertFalse(form.is_valid())
        print(form.errors)  # Print the errors to see which fields are causing issues
        self.assertEqual(len(form.errors), 1)  # Adjust the number of required fields if necessary

    def test_note_form_valid_data(self):
        form = NoteForm(data={
            'title': 'Test Note',
            'content': 'Test Content',
        })
        self.assertTrue(form.is_valid())

    def test_note_form_no_data(self):
        form = NoteForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)  # Adjust the number of required fields if necessary
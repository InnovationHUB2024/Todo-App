# todonote_project/urls.py
from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # For login, logout
    path('signup/', core_views.signup, name='signup'),
    path('activate/<uidb64>/<token>/', core_views.activate, name='activate'),
    path('', core_views.home, name='home'),
    path('todos/', core_views.todo_list, name='todo_list'),
    path('todos/create/', core_views.todo_create, name='todo_create'),
    path('todos/<int:pk>/edit/', core_views.todo_update, name='todo_update'),
    path('todos/<int:pk>/delete/', core_views.todo_delete, name='todo_delete'),
    path('notes/', core_views.note_list, name='note_list'),
    path('notes/create/', core_views.note_create, name='note_create'),
    path('notes/<int:pk>/edit/', core_views.note_update, name='note_update'),
    path('notes/<int:pk>/delete/', core_views.note_delete, name='note_delete'),
]

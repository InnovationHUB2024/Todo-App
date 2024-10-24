"""
URL configuration for django_todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# todonote_project/urls.py
from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login', include('django.contrib.auth.urls')),
    path('login/', core_views.CustomLoginView.as_view(), name='login'),
    path('logout/', core_views.CustomLogoutView.as_view(), name='logout'),
    path('signup/', core_views.signup, name='signup'),
    path('activate/<uidb64>/<token>/', core_views.activate, name='activate'),
    path('', core_views.home, name='home'),
    path('todos/', core_views.todo_list, name='todo_list'),
    path('todos/create/', core_views.todo_create, name='todo_create'),
    path('todos/<int:pk>/update/', core_views.todo_update, name='todo_update'),
    path('todos/<int:pk>/delete/', core_views.todo_delete, name='todo_delete'),
    path('notes/', core_views.note_list, name='note_list'),
    path('notes/create/', core_views.note_create, name='note_create'),
    path('notes/<int:pk>/edit/', core_views.note_update, name='note_update'),
    path('notes/<int:pk>/delete/', core_views.note_delete, name='note_delete'),
]

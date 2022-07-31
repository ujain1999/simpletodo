"""simpletodo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from tasks.views import CreateNewTaskAJAX, DeleteTaskAJAX, EditTaskAJAX, HomeView, MarkAsCompleteViewAJAX
from user_auth.views import LogoutUserView, RegisterView, LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', RegisterView, name='register'),
    path('login', LoginView, name='login'),
    path('logout', LogoutUserView, name='logout'),
    path('', HomeView, name='home-view'),
    path('mark_as_complete', MarkAsCompleteViewAJAX, name='mark-as-complete-ajax'),
    path('create_new_task', CreateNewTaskAJAX, name='create-new-task-ajax'),
    path('delete_task', DeleteTaskAJAX, name='delete-task-ajax'),
    path('edit_task', EditTaskAJAX, name='edit-task-ajax'),
]

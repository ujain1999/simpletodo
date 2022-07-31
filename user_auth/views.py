from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, LoginForm


# Create your views here.


def RegisterView(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            print('Saved User')
            return redirect('login')
        else:
            print('Could not save')
            print(request.POST)
    
    context = {
        'form' : form,
        'form_type' : 'Register',
    }
    return render(request, 'user_auth/register-login.html', context)

def LoginView(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-view')

    context = {
        'form' : form,
        'form_type' : 'Login',
    }
    return render(request, 'user_auth/register-login.html', context)

def LogoutUserView(request):
    logout(request)
    return redirect('login')
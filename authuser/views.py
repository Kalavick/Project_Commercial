from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    if request.method  == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email address and password')


    context = {}
    return render(request, 'authuser_views/auth-login.html', context)

@login_required
def user_logout(request):
    logout(request)
    #return redirect('home')


def authuser(request) :
    # Check to see if loggin in
    breadcrumb = [
        {'label': 'Home', 'url': '/app'},
    ]
    context = {'username': 'username', 'breadcrumb': breadcrumb}
    return render(request, 'authuser_views/index.html', context)

def register(request):
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.created_by = request.user
            user.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})





#def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid email or password")
    else:
        form = LoginForm()
    context = {}
    return render(request, 'authuser_views/auth-login.html', context)
    #return render(request, 'auth-login.html', {'form': form})
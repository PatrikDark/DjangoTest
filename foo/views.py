from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from.forms import UserRegisterForm


def index(request):
    return render(request, 'foo/index.html')


def register(request):
    if request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('register')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'foo/register.html', context)


def login_user(request):
    if request.POST:
        print('in post')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.warning(request, 'Try again with correct credentials')

    return render(request, 'foo/login.html')


@login_required
def profile(request):
    return render(request, 'foo/profile.html')


@login_required
def logout_user(request):
    logout(request)
    return redirect('index')


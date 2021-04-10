from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You logged in successfully', 'success')
                return redirect('posts:all-posts')
            else:
                messages.warning(request, 'username OR password is wrong! Try again.', 'danger')
    else:
        form = UserLoginForm()
        return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'you logged out successfully', 'success')
        return redirect('posts:all-posts')

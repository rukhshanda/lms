from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/dashboard/')
            else:
                messages.error(request, 'Please enter the correct username and password.')
                return redirect('/auth/signin/')
        else:
            messages.error(request, 'Please enter the correct username and password.')
            return redirect('/auth/signin/')
    else:
        if request.user.is_authenticated():
            return redirect('/dashboard/')
        else:
            return render(request, 'auth/login.html', {})


def signout(request):
    logout(request)
    return redirect('/')


def forgot_password(request):
    raise NotImplementedError('This view is not implemented yet.')

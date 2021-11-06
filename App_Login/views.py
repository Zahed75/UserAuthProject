from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.contrib import messages
from .models import *


# Create your views here.


def index(request):
    dict = {}

    return render(request, 'App_Login/home.html', context=dict)


def SignUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            if User.objects.filter(username=username).first():
                messages.success(request, "Username is already taken")
                return redirect('/SignUp/')

            if User.objects.filter(email=email).first():
                messages.success(request, "Email already taken")
                return redirect('/SignUp/')

            user_obj = User(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()
            profile_obj = Profile.objects.create(user=user_obj, username=username, email=email, password=password)
            profile_obj.save()
            return redirect('/login/')

        except Exception as e:
            print(e)

    dict = {}
    return render(request, 'App_Login/register.html', context=dict)


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username).first()

        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/login/')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.warning(request, ' password did not match.')
            return redirect('/login/')

        login(request, user)
        return redirect('/home/')

    dict = {}

    return render(request, 'App_Login/log.html', context=dict)


def logout(request):

    if request.method == "POST":
        logout(request)

    return redirect('home')

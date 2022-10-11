from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        pwd = request.POST['password']

        if username == "" or username == " ":
            messages.info(request, 'Please Enter a Valid Username')
            return redirect('login')

        if pwd == "" or pwd == " ":
            messages.info(request, 'Please Enter a Valid Password')
            return redirect('login')

        user = auth.authenticate(username=username, password=pwd)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid Credentials!')
            return redirect('login')
    else:
        return render(request, 'user_auth/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        cnfpwd = request.POST['cnfpassword']

        if pwd == cnfpwd:
            if username == "" or username == " ":
                messages.info(request, 'Please Enter a Valid Username')
                return redirect('signup')

            if email == "" or email == " ":
                messages.info(request, 'Please Enter a Valid Email \n like abc@example.com')
                return redirect('signup')

            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Used!')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists!')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=pwd)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password are Not Same!')
            return redirect('register')

    return render(request, 'user_auth/signup.html')

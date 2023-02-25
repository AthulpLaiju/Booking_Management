from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth import get_user_model,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from user.models import *

def signup(request):
    user = get_user_model()
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        if user.objects.filter(email=email).exists():
            messages.info(request,'Email already exists!!')
            return redirect('signup')
        else:
            user = user.objects.create_user(username=username, name=name, email=email,phone=phone,password=password )
            user.save()
            print("User created")
            messages.info(request,'Account created successfully')
            return redirect('login')
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request,username=username, password=password)
        print('USER:',user)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'Logged in successfully')
            return redirect('index')
        else:
            messages.info(request,'Invalid Username or Password!!')
            return redirect('login')

    else:
        return render(request,'login.html')
    

def index(request):
    return render(request,'index.html')


def logout(request):
    auth.logout(request)
    return redirect('index')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    else:
        return render(request,'login.html')
def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Your password was successfully updated!')
            return redirect('changepassword')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepassword.html', {
        'form': form
    })







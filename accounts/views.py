from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import login, logout, authenticate

 

# Create your views here.


def signupuser(r):
    if r.method == 'GET':
        return render (r, 'register.html', {'form':UserCreationForm()})
    else:
        if r.POST['password1'] == r.POST['password2']:
            try:
                user = User.objects.create_user(username=r.POST['username'], password=r.POST['password1'])
                user.save()
                login(r, user)
                return  redirect('profile')
            except IntegrityError:
                return render (r,'register.html', {'form':UserCreationForm(), 'error':'Пользователь с таким именем уже существует!'})
        else:
            return render (r, 'register.html', {'form':UserCreationForm(), 'error':'Пароли не совпадают!'})


def profile(r):
    return render (r, 'profile.html')

def logoutuser(r):
    if r.method == 'POST':
        logout(r)
        return redirect('home')

def loginuser(r):
    if r.method == 'GET':
        return render (r, 'loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(r, username=r.POST['username'], password=r.POST['password'])
        if user is None:
            return render (r, 'loginuser.html', {'form':AuthenticationForm(), 'error':'Неверный логин или пароль!'}) 
        else:
            login(r, user)
            return redirect('profile')
        

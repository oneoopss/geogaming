from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
# from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from django.http import JsonResponse
# приветик


# Create your views here.
def home(r):
    if r.method == 'GET':
        return render (r, 'index.html', {'form_reg':UserCreationForm(), 'form_log':AuthenticationForm})
    else:
        try:
            user = authenticate(r, username=r.POST['username'], password=r.POST['password'])
            if user is None:
                return render (r, 'loginuser.html', {'form':AuthenticationForm(), 'error':'Неверный логин или пароль!'}) 
            else:
                login(r, user)
                return redirect('profile')
        except:
            if r.POST['password1'] == r.POST['password2']:
                try:
                    user = User.objects.create_user(username=r.POST['username'], password=r.POST['password1'])
                    user.save()
                    login(r, user)
                    return  redirect('profile')
                except IntegrityError:
                        return render (r,'register.html', {'form_reg':UserCreationForm(), 'form_log':AuthenticationForm,  'error':'Пользователь с таким именем уже существует!'})
            else:
                return render (r, 'register.html', {'form_reg':UserCreationForm(), 'form_log':AuthenticationForm, 'error':'Пароли не совпадают!'})


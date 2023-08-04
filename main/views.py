from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from django.http import JsonResponse



# Create your views here.
def home(r):
    # return render(r, 'index.html',{'form': UserCreationForm})
    if r.method == 'GET':
        return render (r, 'index.html', {'form':UserCreationForm()})
    else:
        if r.POST['password1'] == r.POST['password2']:
            try:
                user = User.objects.create_user(username=r.POST['username'], password=r.POST['password1'])
                user.save()
                login(r, user)
                return  redirect('home')
            except IntegrityError:
                    return render (r,'register.html', {'form':UserCreationForm(), 'error':'Пользователь с таким именем уже существует!'})
        else:
            return render (r, 'index.html', {'form':UserCreationForm(), 'error':'Пароли не совпадают!'})

def posts(r):
    if not r.user.is_authenticated:
        return redirect('home')
    if r.method == 'POST':
        form = PostForm(r.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = r.user
            post.save()
            return redirect('profile')
    else:
        form = PostForm()
    return render(r, 'posts.html', {'form': form})


from django.shortcuts import render, redirect
from .forms import PostForm


# Create your views here.
def home(r):
    return render(r, 'index.html',)

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
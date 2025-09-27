from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .forms import PostForm

def post_list(request):
    q = request.GET.get('q', '')
    posts = Post.objects.all()
    if q:
        posts = posts.filter(models.Q(title__icontains=q) | models.Q(content__icontains=q))
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blogapp/post_list.html', {'posts': posts, 'q': q})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blogapp/post_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(post.get_absolute_url())
    else:
        form = PostForm()
    return render(request, 'blogapp/post_form.html', {'form': form, 'create': True})

@login_required
def post_update(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.author:
        return redirect(post.get_absolute_url())
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(post.get_absolute_url())
    else:
        form = PostForm(instance=post)
    return render(request, 'blogapp/post_form.html', {'form': form, 'create': False})

@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.author:
        return redirect(post.get_absolute_url())
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blogapp/post_confirm_delete.html', {'post': post})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

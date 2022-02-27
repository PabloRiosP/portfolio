from django.shortcuts import render, get_object_or_404
from .models import Blog

def render_posts(request):
    posts = Blog.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Blog, pk=id)
    return render(request, 'post_detail.html', {'post': post})

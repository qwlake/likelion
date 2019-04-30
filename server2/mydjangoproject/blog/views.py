from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'index.html', {'posts_show':posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk = post_id)
    return render(request, 'detail.html', {'post':post_detail})

def new(request):       # write post
    return render(request, 'new.html')

def create(request):    # write post
    post = Post()
    post.title = request.GET['title']
    post.content = request.GET['content']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('/post/' + str(post.id))

def modify(request, post_id):   # edit post
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'modify.html', {'post':post_detail})

def update(request, post_id):   # edit post
    post = get_object_or_404(Post, pk=post_id)
    post.title = request.GET['title']
    post.content = request.GET['content']
    post.save()
    return redirect('/post/' + str(post.id))
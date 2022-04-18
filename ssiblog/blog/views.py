import json
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
from .forms import CommentForm, addPostForm
from django.views.generic import UpdateView, DeleteView
from taggit.models import Tag
from django.core.files.storage import FileSystemStorage


class deletePost(DeleteView):
    model = Post
    template_name = 'deletePost.html'
    success_url = "/"



class updatePost(UpdateView):
    model = Post
    template_name = 'updatePost.html'
    fields = ['title', 'body', 'image', 'tags']


def addPost(request):
    add_Post = addPostForm()

    if request.method == 'POST' and request.FILES:
        upload = request.FILES
        add_Post = addPostForm(request.POST, upload)
        print(add_Post)
        if add_Post.is_valid():
            add_Post.save()
            return redirect("/")

    return render(request, "addPost.html", {'add_Post': add_Post})


def showSinglePost(request, id):
    post = get_object_or_404(Post, slug=id, )
    posts = Post.objects.filter(slug=id)
    comments = Comments.objects.filter(post=posts[0])
    new_comment = None
    print(posts)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            if request.user.is_authenticated:
                new_comment.author = request.user.username
            new_comment.post = get_object_or_404(Post, slug=id, )
            new_comment.save()
            return redirect(post.get_absolute_url())
        else:
            comment_form = CommentForm()
    return render(request, 'singlePost.html', {'posts': posts, 'comments': comments, 'comment_form': comment_form})


def index(request, tag_slug=None):
    posts = Post.objects.all()
    page = request.GET.get('page', 1)
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "index.html", {'posts': posts, 'tag': tag, })

# Create your views here.

import json
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CForm, addPostForm, CommentForm
from django.views.generic import UpdateView, DeleteView
from taggit.models import Tag
from ckeditor.widgets import CKEditorWidget
from django import forms


def seeContactForms(request):
    see = contactForm.objects.all()
    return render(request, "seeContact.html", {'see':see})


def ContactForm(request):
    form = CForm()
    if request.method == "POST":
        form = CForm(data=request.POST)
        print("jej")
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "contact.html", {'form': form})


def approve(request, id):
    id = beforeUser.objects.get(id=id)
    username = id.userName
    print(username)
    emaiL = id.userEmail
    password = id.userPassword
    user = User.objects.create_user(username=username, email=emaiL, password=password)
    user.save()
    id.userActive = 1
    id.save()
    return redirect("/authorize/")


def Register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Hasła się nie są identyczne')
            return render(request, "register.html")
        try:
            new_user = beforeUser.objects.create(userName=username, userPassword=password, userEmail=email)
            new_user.save()
            return redirect(index())
        except:
            pass

    return render(request, "register.html")


def authorize(request):
    users = beforeUser.objects.filter(userActive=0)
    return render(request, 'authorize.html', {'users': users})


def Logout(request):
    logout(request)
    return redirect("/")


def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")

    return render(request, "login.html")


class deletePost(DeleteView):
    model = Post
    template_name = 'deletePost.html'
    success_url = "/"


class updatePost(UpdateView):
    body = forms.CharField(widget=CKEditorWidget())
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

    return render(request, "index.html", {'posts': posts, 'tag': tag, 'page': page})

# Create your views here.

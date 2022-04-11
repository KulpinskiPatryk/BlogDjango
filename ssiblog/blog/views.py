import json
from django.shortcuts import redirect, render, HttpResponse
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


def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {'posts': posts})



# Create your views here.

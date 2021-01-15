from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    context = {
        'posts':Post.objects.all()
        }
    return render(request,'footballnews/home.html',context)

def info(request):
    return render(request,'footballnews/info.html',{'title':"Info"})

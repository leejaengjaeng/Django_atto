from django.shortcuts import render
import application.common.customUserHandler as cuh

# Create your views here.
def news(request):
    posts = cuh.getPosts(request)
    return render(request, "news/news.html",{'posts':posts})

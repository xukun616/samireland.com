from django.shortcuts import render, redirect
from blog.models import BlogPost
import datetime

# Create your views here.

def home_page(request):
    return render(request, "home.html")


def about_page(request):
    return render(request, "about.html")


def new_post_page(request):
    if request.method == "POST":
        BlogPost.objects.create(
         title=request.POST["title"],
         date=datetime.datetime.strptime(
          request.POST["date"], "%Y-%m-%d"
         ).date(),
         body=request.POST["body"],
         visible=request.POST["visible"] == "yes"
        )
        return redirect("/")
    return render(request, "new_post.html")

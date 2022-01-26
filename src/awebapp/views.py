from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from awebapp.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password


def homepage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/awebapp/flux")
    return render(request, "awebapp/homepage.html")

def base(request):
    return render(request, "awebapp/base.html")

def auth_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/awebapp/flux")
    return render(request, "users/login.html")


def auth_logout(request):
    logout(request)
    return render(request, "users/logout.html")

def subscrip(request):
    return render(request, "users/subscrip.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if password == request.POST.get("password_confirm"):
            user=User.objects.create(username=username, password= make_password(password))
            return redirect("/awebapp/login") 
    return render(request, "users/signup.html")

@login_required
def flux(request):
    return render(request, "reviews/flux.html")

@login_required
def posts(request):
    return render(request, "reviews/posts.html")


"""
créer une méthode pour les posts 
1. Créa critique (ticket = review)
2. Commentaire (demander) = critique sur une review
3. Commencer à faire le flux 
"""
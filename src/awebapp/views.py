import re
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from awebapp.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from awebapp.forms import CreateReviewForm, CreateTicketForm
from awebapp.models import User, Ticket, UserFollows, Review


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


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if password == request.POST.get("password_confirm"):
            user = User.objects.create(
                username=username, password=make_password(password)
            )
            return redirect("/awebapp/login")
    return render(request, "users/signup.html")


@login_required
def flux(request):
    tickets = Ticket.objects.all
    reviews = Review.objects.all
    return render(
        request, "reviews/flux.html", {"tickets": tickets, "reviews": reviews}
    )


@login_required
def posts(request):
    reviews = Review.objects.filter(user=request.user)
    tickets = Ticket.objects.filter(user=request.user)
    return render(
        request, "reviews/posts.html", {"reviews": reviews, "tickets": tickets}
    )


@login_required
def abos(request):
    if request.method == "POST":
        username = request.POST.get("username_search")
        followed_user = request.POST.get("followed_user")
        if username:
            try:
                user = User.objects.get(username=username)
            except:
                return render(
                    request,
                    "reviews/abos.html",
                    {"erreur": "Utilisateur non trouvé .."},
                )
            UserFollows.objects.create(user=request.user, followed_user=user)
        elif followed_user:
            UserFollows.objects.get(
                user=request.user, followed_user=followed_user
            ).delete()
    followers = UserFollows.objects.filter(followed_user=request.user)
    followed = UserFollows.objects.filter(user=request.user)
    return render(
        request, "reviews/abos.html", {"followers": followers, "followed": followed}
    )


@login_required
def create_ticket(request):
    if request.method == "POST":
        form_ticket = CreateTicketForm(request.POST, request.FILES)
        if form_ticket.is_valid():
            form_ticket = Ticket.objects.create(
                title=request.POST["title"],
                description=request.POST["description"],
                user=request.user,
                image=request.FILES["image"],
                # time_created=request.TIME["time_created"],
            )
            form_ticket.save()
        #elif form_ticket:
            #Ticket.objects.get(
                #ticket=request.ticket_id
            #).delete()
    else:
        form_ticket = CreateTicketForm(initial={"user": request.user})
        return render(
            request, "reviews/create-ticket.html", {"form_ticket": form_ticket}
        )
    return render(request, "reviews/create-ticket.html")


@login_required
def create_review(request):
    if request.method == "POST":
        form_review = CreateReviewForm(request.POST, request.FILES)
        if form_review.is_valid():
            form_review = Review.objects.create(
                # ticket = form_ticket.get(request.ticket_id),
                rating=request.POST.rating["rating"],
                user=request.user,
                headline=request.POST["headline"],
                body=request.POST["body"],
                # time_created = request.POST["time_created"],
            )
            form_review.save()
        #elif form_review:
            #Review.objects.get(
                #review=request.review_id
            #).delete()
    else:
        form_review = CreateReviewForm(initial={"user": request.user})
        return render(
            request, "reviews/create-review.html", {"form_review": form_review}
        )
    return render(request, "reviews/create-review.html")


"""
@login_required
def create_review(request): #ticket_id):
    form_review = CreateReviewForm()
    form_ticket = CreateTicketForm()
    if request.method == 'POST':
        if form_review in request.POST:
            form_review = CreateReviewForm(request.POST)
            if form_review.is_valid():
                form_review.save()
                return redirect('/awebapp/flux')
            
    else:
            form_review = CreateReviewForm(initial={"user": request.user})
            return render(
                request, "reviews/create-review.html", {"form_review": form_review}
            )
    return render(request, "reviews/create-review.html")
"""


# livre / article doit être différencier dans les forms + model ??
# comment mettre tout dans la même class -> upload / update / delete ??
# faire la creation d'une review en réponse d'un ticket également
# bien gérer l'affichage des images.

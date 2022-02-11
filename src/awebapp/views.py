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
    # abonnés
    followers = UserFollows.objects.filter(followed_user=request.user)
    # abonnements
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
            )
            form_ticket.save()
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
            form_ticket = Ticket.objects.create(
                title=request.POST["title"],
                description=request.POST["description"],
                user=request.user,
                image=request.FILES["image"],
            )
            form_ticket.save()
            form_review = Review.objects.create(
                ticket=form_ticket,
                rating=request.POST["rating"],
                user=request.user,
                headline=request.POST["headline"],
                body=request.POST["body"],
            )
            form_review.save()
    else:
        form_review = CreateReviewForm(initial={"user": request.user})
        return render(
            request, "reviews/create-review.html", {"form_review": form_review}
        )
    return render(request, "reviews/create-review.html")


@login_required
def create_review_ticket(request, id):
    """Création d'une review en réponse à un ticket"""
    if request.method == "POST":
        ticket = Ticket.objects.get(id=id)
        review = Review.objects.create(
            headline=request.POST["headline"],
            body=request.POST["body"],
            user=request.user,
            rating=request.POST["rating"],
            ticket=ticket,
        )
        review.save()
        return render(request, "reviews/posts.html")
    else:
        ticket = Ticket.objects.get(id=id)
        return render(request, "reviews/create-review-ticket.html", {"ticket": ticket})


@login_required
def update_review(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == "POST":
        delete = request.POST.get("delete")
        if delete:
            review.delete()
            return render(request, "reviews/posts.html")
        else:
            form_review = CreateReviewForm(request.POST, request.FILES, initial=review)
            if request.method == "POST":
                review.save()
                return render(request, "reviews/posts.html")
    else:
        form_review = CreateReviewForm(initial=review)
    return render(
        request,
        "reviews/update-review.html",
        {"review": review, "form_review": form_review},
    )


@login_required
def update_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == "POST":
        delete = request.POST.get("delete")
        if delete:
            ticket.delete()
            return render(request, "reviews/posts.html")
        else:
            form_ticket = CreateTicketForm(request.POST, request.FILES, initial=ticket)
            if request.method == "POST":
                ticket.save()
                return render(request, "reviews/posts.html")
    else:
        form_ticket = CreateTicketForm(initial=ticket)
    return render(
        request,
        "reviews/update-ticket.html",
        {"ticket": ticket, "form_ticket": form_ticket},
    )


# livre / article doit être différencier dans les forms + model ??
# comment mettre tout dans la même class -> upload / update / delete ??
# faire la creation d'une review en réponse d'un ticket également
# bien gérer l'affichage des images.

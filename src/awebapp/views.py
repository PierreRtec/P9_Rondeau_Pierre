from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from awebapp.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from awebapp.forms import UploadTicketForm, UploadReviewForm
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
    return render(request, "reviews/posts.html")


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
                    request, "reviews/abos.html", {"erreur": "Utilisateur non trouvé .."}
                )
            UserFollows.objects.create(user=request.user, followed_user=user)
        elif followed_user:
            UserFollows.objects.get(user=request.user, followed_user=followed_user).delete()
    followers = UserFollows.objects.filter(followed_user=request.user)
    followed = UserFollows.objects.filter(user=request.user)
    return render(request, "reviews/abos.html", {"followers": followers, "followed": followed})




@login_required
def create_ticket(request):
    if request.method == "POST":
        form_ticket = UploadTicketForm(request.POST, request.FILES)
        if form_ticket.is_valid():
            form_ticket.save()
    else:
        form_ticket = UploadTicketForm(initial={"user": request.user})
        return render(
            request, "reviews/create-ticket.html", {"form_ticket": form_ticket}
        )


@login_required
def update_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == "POST":
        ticket_update = Ticket.objects.get(id=ticket_id)
        form_ticket = UploadTicketForm(
            request.POST, request.FILES, instance=ticket_update
        )
        if form_ticket.is_valid():
            form_ticket.save()
            return HttpResponseRedirect(reverse("awebapp/posts"))
    else:
        form_ticket = UploadTicketForm(
            initial={
                "user": request.user,
                "title": ticket.title,
                "description": ticket.description,
                "image": ticket.image,
            }
        )
        return render(
            request,
            "reviews/update-ticket.html",
            {"ticket": ticket, "form_ticket": form_ticket},
        )


@login_required
def create_review(request):
    if request.method == "POST":
        form_ticket = UploadTicketForm(request.POST, request.FILES)
        form_review = UploadReviewForm(request.POST)
        if form_ticket.is_valid():
            form_ticket.save()
        ticket = Ticket.objects.filter(user=request.user).latest("time_created")
        headline = request.POST["headline"]
        body = request.POST["body"]
        user = request.user
        rating = request.POST["rating"]
        ticket = ticket
        review = Review.objects.create(
            headline=request.POST["headline"],
            body=request.POST["body"],
            user=request.user,
            rating=request.POST["rating"],
            ticket=ticket,
        )
        return HttpResponseRedirect(reverse("awebapp/posts"))
    else:
        form_ticket = UploadTicketForm(initial={"user": request.user})
        form_review = UploadReviewForm(initial={"user": request.user})
        return render(
            request,
            "reviews/create-review.html",
            {"form_ticket": form_ticket, "form_review": form_review},
        )


@login_required
def update_review(request, review_id):
    if request.method == "POST":
        review_update = Review.objects.get(id=review_id)
        review_update.headline = request.POST["headline"]
        review_update.body = request.POST["body"]
        review_update.rating = request.POST["rating"]
        review_update.save()
        return HttpResponseRedirect(reverse("awebapp/posts"))
    else:
        review = Review.objects.get(id=review_id)
        ticket = Ticket.objects.get(id=review.ticket.id)
        form_review = UploadReviewForm(
            initial={
                "user": request.user,
                "ticket": review.ticket,
                "headline": review.headline,
                "body": review.body,
                "rating": review.rating,
            }
        )
        return render(
            request,
            "reviews/update-review.html",
            {"review": review, "form_review": form_review, "ticket": ticket},
        )


@login_required
def create_review_ticket(request, id):
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
        return HttpResponseRedirect(reverse("awebapp/posts"))
    else:
        ticket = Ticket.objects.get(id=id)
        return render(request, "reviews/create-review-ticket.html", {"ticket": ticket})

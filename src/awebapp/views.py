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
    return render(request, "flux.html", {"tickets": tickets, "reviews": reviews})


@login_required
def posts(request):
    return render(request, "reviews/posts.html")


@login_required
def abos(request):
    following = UserFollows.objects.filter(user=request.user)
    followers = UserFollows.objects.filter(followed_user=request.user)
    return render(
        request, "abos.html", {"following": following, "followers": followers}
    )


"""
@login_required
def update_review(request, review_id):
    if request.method == "POST":
        review_update = Review.objects.get(id=review_id)
        review_update.headline = request.POST["headline"]
        review_update.body = request.POST["body"]
        review_update.rating = request.POST["rating"]
        review_update.save()
        return HttpResponseRedirect(reverse("view-posts"))
    else:
        review = Review.objects.get(id=review_id)
        ticket = Ticket.objects.get(id=review.ticket.id)
        form_review = UploadReviewForm(initial={"user": request.user,
                                                "ticket": review.ticket,
                                                "headline": review.headline,
                                                "body": review.body,
                                                "rating": review.rating,
                                                })
        return render(request, "update-review.html", {"review": review, "form_review": form_review, "ticket": ticket})


@login_required
def update_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == "POST":
        ticket_update = Ticket.objects.get(id=ticket_id)
        form_ticket = UploadTicketForm(request.POST, request.FILES, instance=ticket_update)
        if form_ticket.is_valid():
            form_ticket.save()
            return HttpResponseRedirect(reverse("view-posts"))
    else:
        form_ticket = UploadTicketForm(initial={"user": request.user,
                                                "title": ticket.title,
                                                "description": ticket.description,
                                                "image": ticket.image,
                                                })
        return render(request, "update-ticket.html", {"ticket": ticket, "form_ticket": form_ticket})


@login_required
def add_user_follow(request):
    data_follow = request.POST
    username_search = data_follow["username_search"]
    username_search = User.objects.get(username=username_search)
    user_follow = UserFollows.objects.create(
        user=request.user,
        followed_user=username_search
    )
    user_follow.save()
    return HttpResponseRedirect(reverse("subscribe"))


@login_required
def remove_user_follow(request):
    followed_user = request.POST["followed_user"]
    user_defollow = UserFollows.objects.filter(followed_user=followed_user).filter(user=request.user)
    user_defollow.delete()
    return HttpResponseRedirect(reverse("subscribe"))


@login_required
def create_ticket(request):
    # Method POST
    if request.method == "POST":
        form_ticket = UploadTicketForm(request.POST, request.FILES)
        if form_ticket.is_valid():
            form_ticket.save()
    # Method GET
    else:
        form_ticket = UploadTicketForm(initial={"user": request.user})
        return render(request, "create-ticket.html", {'form_ticket': form_ticket})


@login_required
def create_review(request):
    if request.method == "POST":
        form_ticket = UploadTicketForm(request.POST, request.FILES)
        form_review = UploadReviewForm(request.POST)
        # Form Ticket Saving
        if form_ticket.is_valid():
            form_ticket.save()
        # Form Review Saving
        # Manually adding the data
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
            ticket=ticket
        )
        return HttpResponseRedirect(reverse("view-posts"))
        #return render(request, "test.html", {"data": request.POST, "data_review": review, "data_ticket": ticket})
    else:
        form_ticket = UploadTicketForm(initial={"user": request.user})
        form_review = UploadReviewForm(initial={"user": request.user})
        return render(request, "create-review.html", {"form_ticket": form_ticket, "form_review": form_review})


@login_required
def create_review_ticket(request, id):
    if request.method == "POST":
        ticket = Ticket.objects.get(id=id)
        review = Review.objects.create(
            headline=request.POST["headline"],
            body=request.POST["body"],
            user=request.user,
            rating=request.POST["rating"],
            ticket=ticket
        )
        review.save()
        return HttpResponseRedirect(reverse("view-posts"))
    else:
        ticket = Ticket.objects.get(id=id)
        return render(request, "create-review-ticket.html", {"ticket": ticket})


@login_required
def view_posts(request):
    reviews = Review.objects.filter(user=request.user)
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, "view-posts.html", {"reviews": reviews, "tickets": tickets})
"""

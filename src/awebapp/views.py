from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login
from awebapp.models import User




class IndexView(generic.ListView):
    template_name = "awebapp/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "awebapp/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "awebapp/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "awebapp/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("awebapp:results", args=(question.id,)))

def homepage(request):
    return render(request, "awebapp/homepage.html")

def base(request):
    return render(request, "awebapp/base.html")

def auth_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        login(request, user)
        return redirect("/awebapp/homepage")
    return render(request, "users/login.html")

def logout(request):
    return render(request, "users/logout.html")

def subscrip(request):
    return render(request, "users/subscrip.html")

def signup(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user=User.objects.create(username=username, password=password)
        login(request, user)
        return redirect("/awebapp/homepage")    
    return render(request, "users/signup.html")

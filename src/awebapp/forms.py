from django import forms
from django.forms import ModelForm
from awebapp.models import User, UserFollows, Ticket, Review
from django.core import validators
from django.forms import CharField

class UserForm(ModelForm):

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "password_confirmation",
        ]
        widgets = {
            "password": forms.PasswordInput(),
            "password_confirm": forms.PasswordInput(),
        }


class UserFollowsForm(ModelForm):
    class Meta:
        model = UserFollows
        fields = ["confirm"]
        widgets = {
            "password": forms.PasswordInput(),
            "email": forms.EmailInput(),
        }


class UploadTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image", "user"]
        widgets = {
            "password": forms.PasswordInput(),
            "email": forms.EmailInput(),
        }


class UploadReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["headline", "body", "rating", "ticket", "user"]
        widgets = {
            "headline": forms.PasswordInput(),
            "body": forms.EmailInput(),
            "rating": forms.RatingInput(),
            "ticket": forms.TicketInput(),
        }

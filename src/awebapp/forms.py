from django import forms
from django.forms import Form
from awebapp.models import User, UserFollows, Ticket, Review
from django.core.validators import MaxValueValidator


class User(forms.Form):
    class Meta:
        model = User
        fields = ["username", "password", "password_confirmation"]
        widgets = {
            "password": forms.PasswordInput(),
            "password_confirm": forms.PasswordInput(),
        }


class UserFollowsForm(forms.Form):
    class Meta:
        model = UserFollows
        fields = ["user", "followed_user"]
        labels = {"followed_user": "Utilisateur à suivre :"}
        exclude = ["user"]


class CreateTicketForm(forms.Form):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image", "user"]


class UploadReviewForm(forms.Form):
    class Meta:
        model = Review
        rating = forms.ChoiceField(
            widget=forms.RadioSelect, choices=[(note, note) for note in range(1, 6)]
        )
        fields = ["headline", "body", "rating", "ticket", "user"]

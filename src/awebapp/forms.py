
from django.forms import ModelForm
from django import forms
from awebapp.models import User, UserFollows, Ticket, Review


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirmation',]
        widgets = {
            'password': forms.PasswordInput(),
            'password_confirm': forms.PasswordInput(),
        }


class UserFollowsForm(ModelForm):

    class Meta:
        model = UserFollows
        fields = ['confirm']

class UploadTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ["title", "description", "image", "user"]
        widgets = {
            'title': forms.TitleField(),
            'description': forms.DescriptionField(),
            'image': forms.ImageField(),
            'user': forms.User(),
        }

class UploadReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ["headline", "body", "rating", "ticket", "user"]
        widgets = {
            'headline': forms.PasswordInput(),
            'body': forms.EmailInput(),
            'rating': forms.RatingInput(),
            'ticket': forms.TicketInput(),
        }
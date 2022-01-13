
from django.forms import ModelForm
from django import forms
from awebapp.models import User, UserFollows

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name']
        widgets = {
            'password': forms.PasswordInput(),
            'first_name': forms.PasswordInput(),
        }


class UserFollowsForm(ModelForm):

    class Meta:
        model = UserFollows
        fields = ['confirm']
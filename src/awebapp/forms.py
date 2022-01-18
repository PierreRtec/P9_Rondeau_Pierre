
from django.forms import ModelForm
from django import forms
from awebapp.models import User, UserFollows

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(),
        }


class UserFollowsForm(ModelForm):

    class Meta:
        model = UserFollows
        fields = ['confirm']
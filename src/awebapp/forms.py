
from django.forms import ModelForm
from django import forms
from awebapp.models import User, UserFollows

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'password_confirmation']
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(),
            'password_confirm': forms.PasswordInput(),
        }


class UserFollowsForm(ModelForm):

    class Meta:
        model = UserFollows
        fields = ['confirm']

"""
crea des forms adaptés aux modèles / view
"""
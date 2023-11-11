from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from django import forms
from crispy_forms.helper import FormHelper
from django.forms import ModelForm
from .models import UserProfile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    # def __init__(self, *args, **kwargs):
        # super(SignUpForm, self).__init__(*args, **kwargs)
        #
        # for fieldname in ['username', 'password1', 'password2']:
            # fields[fieldname].help_text = None

class UserForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"
        exclude = ['user']
        labels = {
            'profile_img' : 'Profile Image'
        }


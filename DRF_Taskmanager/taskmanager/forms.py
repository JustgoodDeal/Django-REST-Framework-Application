from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('__all__')

class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

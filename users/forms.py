from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'Roll_No', 'Date_Of_Birth']
        widgets = {
            'Date_Of_Birth': forms.DateInput(attrs={'type': 'date'}),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'Roll_No', 'Date_Of_Birth']
        widgets = {
            'Date_Of_Birth': forms.DateInput(attrs={'type': 'date'}),
        }

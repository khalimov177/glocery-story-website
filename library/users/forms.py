from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from app.bulma_mixin import BulmaMixin
from django.contrib.auth.forms import PasswordChangeForm

class SignUpForm(BulmaMixin,UserCreationForm):
    email = forms.EmailField(label='write your email')
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['email','password']

class SignInForm(BulmaMixin,AuthenticationForm):
    email = forms.EmailField(label='write your email')
    password = forms.PasswordInput()
    
    class Meta:
        model = User
        fields = ['email' , 'password']


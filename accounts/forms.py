from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DonorSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=250, help_text='e.g youremail@gmail.com')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class SignInForm(forms.Form):
    email = forms.EmailField(label='Email address', widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'id': 'form2Example17'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'id': 'form2Example27'}))

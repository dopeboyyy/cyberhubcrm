from crispy_forms.helper import FormHelper
from allauth.account.forms import LoginForm, SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class UserLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['login'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'username'})
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Password', 'id': 'password'})
        self.fields['remember'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})


class UserRegistrationForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control mb-1', 'placeholder': 'Email', 'id': 'email'})
        self.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-1', 'placeholder': 'Username', 'id': 'username1'})
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-1', 'placeholder': 'New Password', 'id': 'password1'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-1', 'placeholder': 'New Password Again', 'id': 'password2'})
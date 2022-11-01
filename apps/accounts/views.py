from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Login(LoginRequiredMixin, TemplateView):
    template_name = "account/login.html"


class Register(LoginRequiredMixin, TemplateView):
    template_name = "account/signup.html"
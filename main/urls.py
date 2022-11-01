"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from django.contrib import admin
from django.urls import path, include
from main import views
from django.views.generic import TemplateView
from .views import MyPasswordSetView, MyPasswordChangeView
from django.contrib.auth.decorators import login_required
from apps.accounts.views import Login, Register

urlpatterns = [
    path('admin/', admin.site.urls),
    # Index
    path('', views.Index.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),

    # Allauth
    path('accounts/', include('allauth.urls')),
    # Extras
    # logout
    path('logout/', TemplateView.as_view(template_name="account/logout-success.html"), name="logout"),
    # Custom change password done page redirect
    path('accounts/password/change/', login_required(MyPasswordChangeView.as_view()), name="account_change_password"),
    # Custom set password done page redirect
    path('accounts/password/set/', login_required(MyPasswordSetView.as_view()), name="account_set_password"),

]

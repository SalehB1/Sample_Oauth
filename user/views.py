# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView
# from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from .models import User


def login():
    pass

def signup():
    pass
import random

from django import forms
from django.forms import TextInput
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy


class LoginFrom(forms.Form):
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "input100", 'type': "text", 'name': "phone", 'placeholder': "شماره همراه"}))

    password = forms.CharField(strip=False,
                               widget=forms.PasswordInput(
                                   attrs={'class': "input100", 'type': "password", 'name': "pass",
                                          'placeholder': "رمز عبور"}))


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label=gettext_lazy("رمز عبور"), strip=False,
        widget=forms.PasswordInput(attrs={'class': "input100",
                                          'placeholder': "رمز عبور"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=gettext_lazy("تایید رمز عبور"), strip=False,
        widget=forms.PasswordInput(attrs={'class': "input100",
                                          'placeholder': "تایید رمز عبور"}),

        help_text=gettext_lazy("برای تایید همان رمز عبور قبلی را وارد کنید."),
    )
    #
    # phone = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={'class': "input100", 'type': "text", 'name': "phone", 'placeholder': "شماره همراه"}))

    class Meta:
        model = User
        fields = ("phone", "password1", "password2")
        widgets = {
            'phone': TextInput(
                attrs={'class': "input100", 'placeholder': "شماره همراه یا ایمیل"}),
        }

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        if "@" in self.cleaned_data['phone']:
            user.email = self.cleaned_data['phone']
            user.phone = None
        else:
            user.phone = self.cleaned_data['phone']
            user.email = None
        user.is_verified = False
        if commit:
            user.save()
        return user

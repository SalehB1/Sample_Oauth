# Create your views here.
from .forms import RegisterForm, LoginFrom
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView


@login_required()
def index(request):
    return render(request, "home.html", {'user': request.user})


def user_login(request):
    if request.method == 'POST':
        form = LoginFrom(request.POST)
        print('form')
        if form.is_valid():
            clean_data = form.cleaned_data
            user = authenticate(email=clean_data['phone'], password=clean_data['password'])
            print('user')
            if user is not None:
                print('active')
                if user.is_active:
                    login(request, user)
                    print('im in site hooray!!')
                    return redirect('home')
            else:
                messages.info(request, "ورود ناموفق ، اطلاعات خود را چک کنید ")
    else:
        form = LoginFrom()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    if request.method == "GET":
        logout(request)
        messages.info(request, "با موفقیت خارج شدید")
        return redirect('user_login')


class UserSignup(CreateView):
    template_name = 'signup.html'
    success_url = reverse_lazy("sellerLogin")
    from_class = RegisterForm
    success_message = "شما با موفقیت ثبت نام کردید"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "ثبت نام با موفقیت انجام شد.")
            return redirect('home')
        messages.error(request, "ورودی نامعتبر !")
        return redirect('user_signup')

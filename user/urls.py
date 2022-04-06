from django.urls import path
# from .views import SupplierLogin, SellerLogout, SellerRegister
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('user/login/', user_login, name="user_login"),
    path('user/logout/', user_logout, name="user_logout"),
    path('user/signup/', UserSignup.as_view(), name="user_signup"),

]

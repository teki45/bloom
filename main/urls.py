from django.urls import path
from .views import *

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("signup/", SignUp.as_view(), name="signup"),
    path("signin/", SignIn.as_view(), name="signup"),
]

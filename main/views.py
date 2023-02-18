from django.shortcuts import render
from django.views import View

class Home(View):
    def get(self, request):
        return render(request, "home.html")

class SignUp(View):
    def get(self, request):
        return render(request, "auth/signup.html")

class SignIn(View):
    def get(self, request):
        return render(request, "auth/signin.html")


from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, base_user

# Create your views here.

class Login(View):
    def get(self, request):
        request.session["user"] = ""
        return render(request, "login2.html", {})

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            # login succeeds, redirects to homepage
            login(request, user)
            return redirect("/home/")
        else:
            # login fails, credentials are incorrect
            fail_message = "username or password is invalid"
            return render(request, "login2.html",{"fail_message": fail_message})

class Home(View):
    def get(self, request):
        return render(request, "home2.html", {})

    def post(self, request):
        return render(request, "home2.html", {})

class AddUser(View):
    def get(self, request):
        return render(request, "adduser.html", {})

    def post(self, request):
        return render(request, "adduser.html", {})
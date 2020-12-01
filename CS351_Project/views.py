from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from .models import MyUser

# Create your views here.

# *** ADMIN/SUPERUSER LOGIN ***
# username: admin
# password: admin

class Login(View):
    def get(self, request):
        request.session["user"] = ""
        return render(request, "login2.html", {})

    # vvv Referenced: https://stackoverflow.com/questions/38771004/how-to-create-separate-login-for-admin-and-user-in-django
    def post(self, request):
        username = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            # login succeeds, redirects to homepage
            request.session["user"] = request.POST["name"]
            #login(request, user)
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
        users = map(str, list(MyUser.objects.all()))
        return render(request, "adduser.html", {"users": users})

    def post(self, request):
        name = request.POST.get("name","")
        password = request.POST.get("password","")
        if name & password != "":
            newUser = MyUser(name=name, password=password)
            newUser.save()

        users = map(str, list(MyUser.objects.all()))

        return render(request, "adduser.html", {"users": users})
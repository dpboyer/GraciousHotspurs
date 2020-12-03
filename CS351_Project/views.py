from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import UserForm, CoursesForm, SectionsForm
from .models import Instructor, Course, Section

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
        form = UserForm()
        users = map(str, list(User.objects.all()))
        return render(request, 'adduser.html', {"form": form, "users": users})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            # assigns field data from form to variables
            usern = form.cleaned_data['username']
            passw = form.cleaned_data['password']
            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            eml = form.cleaned_data['email']
            phn = form.cleaned_data['phone_number']

            # vvv For debugging
            print(usern, passw, first, last, eml, phn)

            # assigns attributes to a User object and saves it to the database
            newUser = User(username=usern, password=passw, first_name=first, last_name=last, email=eml) #phone_number=phn)
            newUser.save()

            # gives a list of all current User objects
            users = map(str, list(User.objects.all()))
            return render(request, 'adduser.html', {"form": form, "users": users})
        else:
            return render(request, 'adduser.html', {"form": form})


# vvv Referenced: https://www.educba.com/django-forms/
class Courses(View):
    def get(self, request):
        form = CoursesForm()
        courses = map(str, list(Course.objects.all()))
        return render(request, 'courses.html', {"form": form, "courses": courses})

    def post(self, request):
        form = CoursesForm(request.POST)
        if form.is_valid():
            # assigns field data from form to variables
            dept = form.cleaned_data['department']
            crse = form.cleaned_data['course_num']

            # vvv For debugging
            print(dept, crse)

            # assigns attributes to a Course object and saves it to the database
            newCourse = Course(department=dept, course_num=crse)
            newCourse.save()

            # gives a list of all current Course objects
            courses = map(str, list(Course.objects.all()))
            return render(request, 'courses.html', {"form": form, "courses": courses})
        else:
            return render(request, 'courses.html', {"form": form})


class Sections(View):
    def get(self, request):
        form = SectionsForm()
        sections = map(str, list(Section.objects.all()))
        return render(request, 'sections.html', {"form": form, "sections": sections})

    def post(self, request):
        form = SectionsForm(request.POST)
        if form.is_valid():
            # assigns field data from form to variables
            crse = form.cleaned_data['course']
            sect = form.cleaned_data['section_num']

            # vvv For debugging
            print(crse, sect)

            # assigns attributes to a Course object and saves it to the database
            newSection = Section(course=crse, section_num=sect)
            newSection.save()

            # gives a list of all current Course objects
            sections = map(str, list(Section.objects.all()))
            return render(request, 'sections.html', {"form": form, "sections": sections})
        else:
            return render(request, 'sections.html', {"form": form})

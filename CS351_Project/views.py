from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import UserForm, CoursesForm, CoursesDeleteForm, SectionsForm, SectionsDeleteForm, AccountForm
from .models import Instructor, Course, Section, TA

# Create your views here.

# *** ADMIN/SUPERUSER LOGIN ***
# username: admin
# password: admin

decorators = [login_required]

class Login(View):
    def get(self, request):
        logout(request)
        request.session["user"] = ""
        return render(request, "login2.html", {})

    # vvv Referenced: https://stackoverflow.com/questions/38771004/how-to-create-separate-login-for-admin-and-user-in-django
    def post(self, request):
        username = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login succeeds, redirects to homepage
            request.session["user"] = request.POST["name"]
            login(request, user)
            print(request.user)
            return redirect("/home/")
        else:
            # login fails, credentials are incorrect
            fail_message = "username or password is invalid"
            return render(request, "login2.html",{"fail_message": fail_message})


@method_decorator(decorators, name='get')
class Home(View):
    def get(self, request):
        return render(request, "home2.html", {})

    def post(self, request):
        return render(request, "home2.html", {})


@method_decorator(decorators, name='get')
class Account(View):
    def get(self, request):
        form = AccountForm()
        return render(request, "account.html", {"form": form})

    def post(self, request):
        form = AccountForm(request.POST)
        if form.is_valid():
            # assigns field data from form to variables
            phone = form.cleaned_data['phone_number']
            hours = form.cleaned_data['office_hours']
            number = form.cleaned_data['office_number']
            location = form.cleaned_data['office_location']

            currentUser = request.user

            return render(request, 'account.html', {"form": form})
        else:
            return render(request, 'account.html', {"form": form})


@method_decorator(decorators, name='get')
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

            # assigns attributes to a User object and saves it to the database
            # also assigns created User attributes of TA or Instructor object and saves it to the database
            if request.POST['selection'] == 'addTA':
                newUser = User(username=usern, password=passw, first_name=first, last_name=last, email=eml)
                newUser.save()
                newTA = TA(user = newUser)
                newTA.save()
            elif request.POST['selection'] == 'addInstructor':
                newUser = User(username=usern, password=passw, first_name=first, last_name=last, email=eml)
                newUser.save()
                newInstructor= Instructor(user = newUser)
                newInstructor.save()


            # gives a list of all current User objects
            users = map(str, list(User.objects.all()))
            return render(request, 'adduser.html', {"form": form, "users": users})
        else:
            return render(request, 'adduser.html', {"form": form})


# vvv Referenced: https://www.educba.com/django-forms/
@method_decorator(decorators, name='get')
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
            crse = form.cleaned_data['course_number']
            instructor = form.cleaned_data['instructor']

            # assigns attributes to a Course object and saves it to the database
            newCourse = Course(department=dept, course_num=crse, instructor=instructor)
            newCourse.save()

            # gives a list of all current Course objects
            courses = map(str, list(Course.objects.all()))
            return render(request, 'courses.html', {"form": form, "courses": courses})
        else:
            return render(request, 'courses.html', {"form": form})


@method_decorator(decorators, name='get')
class DelCourse(View):
    def get(self, request):
        form = CoursesDeleteForm()
        courses = map(str, list(Course.objects.all()))
        return render(request, 'delcourse.html', {"form": form, "courses": courses})

    def post(self, request):
        form = CoursesDeleteForm(request.POST)
        if form.is_valid():
            # assigns field data from form to variables
            crse = form.cleaned_data['course_number']

            # deletes selected course and displays updated list
            crse.delete()
            courses = map(str, list(Course.objects.all()))
            return render(request, 'delcourse.html', {"form": form, "courses": courses})

        else:
            return render(request, 'delcourse.html', {"form": form})


@method_decorator(decorators, name='get')
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
            sect = form.cleaned_data['section_number']
            teachingAssistant = form.cleaned_data['teaching_assistant']

            # assigns attributes to a Course object and saves it to the database
            newSection = Section(course=crse, section_num=sect, teachingAssistant=teachingAssistant)
            newSection.save()

            # gives a list of all current Course objects
            sections = map(str, list(Section.objects.all()))
            return render(request, 'sections.html', {"form": form, "sections": sections})
        else:
            return render(request, 'sections.html', {"form": form})


@method_decorator(decorators, name='get')
class DelSection(View):
    def get(self, request):
        form = SectionsDeleteForm()
        sections = map(str, list(Section.objects.all()))
        return render(request, 'delsection.html', {"form": form, "sections": sections})

    def post(self, request):
        form = SectionsDeleteForm(request.POST)

        if form.is_valid():
            sect = form.cleaned_data['section_number']

            sect.delete()
            sections = map(str, list(Section.objects.all()))
            return render(request, 'delsection.html', {"form": form, "sections": sections})
        else:
            return render(request, 'delsection.html', {"form": form})


class Syllabus(View):
    def get(self, request, *args, **kwargs):
        course_value = kwargs['course']
        section_value = kwargs['section']
        syllabus_data = self.get_syllabus(course_value,section_value)
        return render(request, "syllabus.html", {'syllabus': syllabus_data})

    def get_syllabus(self, course, section):
        course_instance = Course.objects.filter(course_num=course)
        section_instance = Section.objects.filter(section_num=section, course=course_instance)
        return {'found': False}


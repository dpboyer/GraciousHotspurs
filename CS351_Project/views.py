from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import UserForm, UsersDeleteForm, CoursesForm, CoursesDeleteForm, SectionsForm, SectionsDeleteForm, AccountForm
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
        username = request.POST.get("name", "")
        password = request.POST.get("password", "")
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
        currentUser = request.user

        # initialize currentTA and currentInstr
        currentTA = TA()
        currentInstr = Instructor()
        currentSections = Section()
        currentCourses = Course()

        try:
            currentTA = TA.objects.get(user=currentUser)
            currentSections = Section.objects.filter(teachingAssistant=currentTA)
        except TA.DoesNotExist:
            currentTA = None

        if currentTA is None:
            # get current User's Instructor object
            try:
                currentInstr = Instructor.objects.get(user=currentUser)
                currentCourses = Course.objects.filter(instructor=currentInstr)
            except Instructor.DoesNotExist:
                currentInstr = None

        return render(request, "home2.html", {"ta": currentTA, "instr": currentInstr,
            "courses": currentCourses, "sections": currentSections})

    def post(self, request):
        return render(request, "home2.html", {})


@method_decorator(decorators, name='get')
class Account(View):
    def get(self, request):
        if request.user.is_superuser:
            return redirect("/home/")
        form = AccountForm()
        currentUser = request.user

        # initialize currentTA and currentInstr
        currentTA = TA()
        currentInstr = Instructor()

        # vvv determines which info needs to display, either TA or Instructor
            # get current User's TA object
        try:
            currentTA = TA.objects.get(user=currentUser)
        except TA.DoesNotExist:
            currentTA = None

        # look for Instructor object, if there was no TA
        if currentTA is None:
            # get current User's Instructor object
            try:
                currentInstr = Instructor.objects.get(user=currentUser)
            except Instructor.DoesNotExist:
                currentInstr = None

        return render(request, "account.html", {"form": form, "taInfo": currentTA, "instrInfo": currentInstr})

    def post(self, request):
        form = AccountForm(request.POST)
        if form.is_valid():
            # assigns field data from form to variables
            phone = form.cleaned_data['phone_number']
            hours = form.cleaned_data['office_hours']
            number = form.cleaned_data['office_number']
            location = form.cleaned_data['office_location']

            currentUser = request.user

            # initialize currentTA and currentInstr
            currentTA = TA()
            currentInstr = Instructor()

            # vvv determines which info needs to be edited or displayed, either TA or Instructor
            try:
                currentTA = TA.objects.get(user=currentUser)

                # guarantees that current values are NOT changed if its corresponding field is left empty
                if self.field_not_empty(phone):
                    currentTA.phone_number = phone
                if self.field_not_empty(hours):
                    currentTA.office_hour = hours
                if self.field_not_empty(number):
                    currentTA.office_number = number
                if self.field_not_empty(location):
                    currentTA.office_location = location

                currentTA.save()
            except TA.DoesNotExist:
                currentTA = None

            if currentTA is None:
                try:
                    currentInstr = Instructor.objects.get(user=currentUser)

                    # guarantees that current values are NOT changed if its corresponding field is left empty
                    if self.field_not_empty(phone):
                        currentInstr.phone_number = phone
                    if self.field_not_empty(hours):
                        currentInstr.office_hour = hours
                    if self.field_not_empty(number):
                        currentInstr.office_number = number
                    if self.field_not_empty(location):
                        currentInstr.office_location = location

                    currentInstr.save()
                except Instructor.DoesNotExist:
                    currentInstr = None

            return render(request, 'account.html', {"form": form, "taInfo": currentTA, "instrInfo": currentInstr})
        else:
            return render(request, 'account.html', {"form": form})

    # if a passed field is empty, return false. Otherwise, true.
    def field_not_empty(self, field):
        if field == '':
            return False
        return True


@method_decorator(decorators, name='get')
class AddUser(View):
    def get(self, request):
        if not request.user.is_superuser:
            return redirect("/home/")
        form = UserForm()
        users = User.objects.all()
        instructors = Instructor.objects.all()
        tas = TA.objects.all()
        return render(request, 'adduser.html', {"form": form, "users": users, "instructors": instructors,
                                                    "teachingAssistants": tas})

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

            if request.POST['selection'] == 'Add as Instructor':
                newUser = User(username=usern, password=passw, first_name=first, last_name=last, email=eml)
                newUser.save()
                newInstructor= Instructor(user = newUser)
                newInstructor.save()
            elif request.POST['selection'] == 'Add as TA':
                newUser = User(username=usern, password=passw, first_name=first, last_name=last, email=eml)
                newUser.save()
                newTA = TA(user = newUser)
                newTA.save()

            # gives a list of all current User objects
            users = User.objects.all()
            instructors = Instructor.objects.all()
            tas = TA.objects.all()
            return render(request, 'adduser.html', {"form": form, "users": users, "instructors": instructors,
                                                    "teachingAssistants": tas})
        else:
            return render(request, 'adduser.html', {"form": form})


@method_decorator(decorators, name='get')
class DelUser(View):
    def get(self, request):
        if not request.user.is_superuser:
            return redirect("/home/")
        form = UsersDeleteForm()
        users = User.objects.all()
        instructors = Instructor.objects.all()
        tas = TA.objects.all()
        return render(request, 'deluser.html', {"form": form, "users": users, "instructors": instructors,
                                                    "teachingAssistants": tas})

    def post(self, request):
        form = UsersDeleteForm(request.POST)
        if form.is_valid():
            # assigns field data from form to variables
            user_to_delete = form.cleaned_data['user_to_delete']

            # deletes selected course and displays updated list
            user_to_delete.delete()
            users = User.objects.all()
            instructors = Instructor.objects.all()
            tas = TA.objects.all()
            return render(request, 'deluser.html', {"form": form, "users": users, "instructors": instructors,
                                                    "teachingAssistants": tas})

        else:
            return render(request, 'delcourse.html', {"form": form})


# vvv Referenced: https://www.educba.com/django-forms/
@method_decorator(decorators, name='get')
class Courses(View):
    def get(self, request):
        if not request.user.is_superuser:
            return redirect("/home/")
        form = CoursesForm()
        courses = Course.objects.all()
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
            courses = Course.objects.all()
            return render(request, 'courses.html', {"form": form, "courses": courses})
        else:
            return render(request, 'courses.html', {"form": form})


@method_decorator(decorators, name='get')
class DelCourse(View):
    def get(self, request):
        if not request.user.is_superuser:
            return redirect("/home/")
        form = CoursesDeleteForm()
        courses = Course.objects.all()
        return render(request, 'delcourse.html', {"form": form, "courses": courses})

    def post(self, request):
        form = CoursesDeleteForm(request.POST)
        if form.is_valid():
            # assigns field data from form to variables
            crse = form.cleaned_data['course_number']

            # deletes selected course and displays updated list
            crse.delete()
            courses = Course.objects.all()
            return render(request, 'delcourse.html', {"form": form, "courses": courses})

        else:
            return render(request, 'delcourse.html', {"form": form})


@method_decorator(decorators, name='get')
class Sections(View):
    def get(self, request):
        if not request.user.is_superuser:
            return redirect("/home/")
        form = SectionsForm()
        sections = Section.objects.all()
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

            # gives a list of all current Section objects
            sections = Section.objects.all()
            return render(request, 'sections.html', {"form": form, "sections": sections})
        else:
            return render(request, 'sections.html', {"form": form})


@method_decorator(decorators, name='get')
class DelSection(View):
    def get(self, request):
        if not request.user.is_superuser:
            return redirect("/home/")
        form = SectionsDeleteForm()
        sections = Section.objects.all()
        return render(request, 'delsection.html', {"form": form, "sections": sections})

    def post(self, request):
        form = SectionsDeleteForm(request.POST)

        if form.is_valid():
            sect = form.cleaned_data['section_number']

            sect.delete()
            sections = Section.objects.all()
            return render(request, 'delsection.html', {"form": form, "sections": sections})
        else:
            return render(request, 'delsection.html', {"form": form})


class Syllabus(View):
    def get(self, request, *args, **kwargs):
        if kwargs == {}:
            return render(request, "syllabus.html", {'syllabus': 'make_list'})
        course_value = kwargs['course']
        section_value = kwargs['section']
        syllabus_data = self.get_syllabus_from_model(course_value, section_value)
        return render(request, "syllabus.html", {'syllabus': syllabus_data})

    def get_syllabus_from_model(self, course, section):
        course_instance = Course.get_instructor_by_course_num(course)
        section_instance = Section.get_TA_by_course_and_section(course_instance, section)
        personal_info = {
            'instructors_info': course_instance.get_instructor_personal_info(),
            'teachingAssistantInfo': section_instance.get_TA_personal_info()
        }
        return {'found': True, 'info': personal_info}


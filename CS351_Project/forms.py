from django import forms
from .models import Course, Section, Instructor, TA

class CoursesForm(forms.Form):
    instructor = forms.ModelChoiceField(queryset=Instructor.objects.all())
    department = forms.CharField(max_length=20)
    course_number = forms.CharField(max_length=3)

class CoursesDeleteForm(forms.Form):
    course_number = forms.ModelChoiceField(queryset=Course.objects.all())

class SectionsForm(forms.Form):
    teaching_assistant = forms.ModelChoiceField(queryset=TA.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    section_number = forms.CharField(max_length=3)

class SectionsDeleteForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    section_number = forms.ModelChoiceField(queryset=Section.objects.all())

class UserForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.CharField(max_length=20)

class AccountForm(forms.Form):
    phone_number = forms.CharField(max_length=20)
    office_hours = forms.CharField(max_length=20)
    office_number = forms.CharField(max_length=20)
    office_location = forms.CharField(max_length=20)


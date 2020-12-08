from django import forms
from .models import Course, Section

class CoursesForm(forms.Form):
    department = forms.CharField(max_length=20)
    course_number = forms.CharField(max_length=3)

class CoursesDeleteForm(forms.Form):
    course_number = forms.ModelChoiceField(queryset=Course.objects.all())

class SectionsForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    section_number = forms.CharField(max_length=3)

class SectionsDeleteForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    section_number = forms.ModelChoiceField(queryset=Section.objects.all())

class UserForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.CharField(max_length=20)

class AccountForm(forms.Form):
    phone_number = forms.CharField(max_length=20)
    office_hours = forms.CharField(max_length=20)
    office_number = forms.CharField(max_length=20)
    office_location = forms.CharField(max_length=20)


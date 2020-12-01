from django import forms

class CoursesForm(forms.Form):
    department = forms.CharField(max_length=20)
    course_num = forms.CharField(max_length=3)

class UserForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.CharField(max_length=20)
    phone_number = forms.CharField(max_length=20)
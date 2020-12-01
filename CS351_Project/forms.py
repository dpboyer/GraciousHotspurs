from django import forms

class CoursesForm(forms.Form):
    department = forms.CharField(max_length=20)
    course_num = forms.CharField(max_length=3)
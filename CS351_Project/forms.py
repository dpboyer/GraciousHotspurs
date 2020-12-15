from django import forms
from .models import Course, Section, Instructor, TA


class CoursesForm(forms.Form):
    instructor = forms.ModelChoiceField(queryset=Instructor.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-select', })
                                        )
    department = forms.CharField(max_length=20,
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control',
                                         'placeholder': 'Department',
                                     }
                                 )
                                 )
    course_number = forms.CharField(max_length=3,
                                    widget=forms.TextInput(
                                        attrs={
                                            'class': 'form-control',
                                            'placeholder': '111',
                                        }
                                    )
                                    )


class CoursesDeleteForm(forms.Form):
    course_number = forms.ModelChoiceField(queryset=Course.objects.all(),
                                           widget=forms.Select(attrs={'class': 'form-select', })
                                           )


class SectionsForm(forms.Form):
    teaching_assistant = forms.ModelChoiceField(queryset=TA.objects.all(),
                                                widget=forms.Select(attrs={'class': 'form-select', })
                                                )
    course = forms.ModelChoiceField(queryset=Course.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-select', })
                                    )
    section_number = forms.CharField(max_length=3,
                                     widget=forms.TextInput(
                                         attrs={
                                             'class': 'form-control',
                                             'placeholder': 'username',
                                         }
                                     )
                                     )


class SectionsDeleteForm(forms.Form):
    section_number = forms.ModelChoiceField(queryset=Section.objects.all(),
                                            widget=forms.Select(attrs={'class': 'form-select', })
                                            )


class UserForm(forms.Form):
    username = forms.CharField(max_length=20,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'username',
                                   }
                               )
                               )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '**********',
        }
    )
    )
    first_name = forms.CharField(max_length=20,
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control',
                                         'placeholder': 'First Name',
                                     }
                                 )
                                 )
    last_name = forms.CharField(max_length=20,
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Last Name',
                                    }
                                )
                                )
    email = forms.CharField(max_length=20,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'you@email.com',
                                }
                            )
                            )


class AccountForm(forms.Form):
    phone_number = forms.CharField(max_length=20, required=False,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'form-control',
                                           'placeholder': 'Enter Phone Number'
                                       }
                                   )
                                   )
    office_hours = forms.CharField(max_length=20, required=False,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'form-control',
                                           'placeholder': 'Enter Office Hours',
                                       }
                                   )
                                   )
    office_number = forms.CharField(max_length=20, required=False,
                                    widget=forms.TextInput(
                                        attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Enter Office Number',
                                        }
                                    )
                                    )
    office_location = forms.CharField(max_length=20, required=False,
                                      widget=forms.TextInput(
                                          attrs={
                                              'class': 'form-control',
                                              'placeholder': 'Enter Office Location',
                                          }
                                      )
                                      )

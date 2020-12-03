from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# *** MyUser will be refactored
class MyUser(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    #first_name = models.CharField(max_length=20)
    #last_name = models.CharField(max_length=20)
    #email = models.CharField(max_length=20)
    #phone_number = models.CharField(max_length=20)


    def __str__(self):
        return self.name + self.password

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)

class Course(models.Model):
    #course_key = models.CharField(max_length=20, primary_key=True, default='')
    department = models.CharField(max_length=20)
    course_num = models.CharField(max_length=3)


class Section(models.Model):
    course = models.ForeignKey(to="Course", on_delete=models.CASCADE)
    section_num = models.CharField(max_length=3)


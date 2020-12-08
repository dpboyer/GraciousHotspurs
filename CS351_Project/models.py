from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Course(models.Model):
    department = models.CharField(max_length=20)
    course_num = models.CharField(max_length=3)

    def __str__(self):
        return self.department + " " + self.course_num


class Section(models.Model):
    course = models.ForeignKey(to="Course", on_delete=models.CASCADE)
    section_num = models.CharField(max_length=3)

    def __str__(self):
        return self.course.department + " " + self.course.course_num + "-" + self.section_num


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=20, default="", blank=True)
    office_hour = models.CharField(max_length=20, default="", blank=True)
    office_number = models.CharField(max_length=20, default="", blank=True)
    office_location = models.CharField(max_length=20, default="", blank=True)


class TA(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=20, default="", null=True)
    office_hour = models.CharField(max_length=20, default="", null=True)
    office_number = models.CharField(max_length=20, default="", null=True)
    office_location = models.CharField(max_length=20, default="", null=True)


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

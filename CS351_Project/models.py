from django.db import models
from django.contrib.auth.models import User


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20, default="", blank=True)
    office_hour = models.CharField(max_length=20, default="", blank=True)
    office_number = models.CharField(max_length=20, default="", blank=True)
    office_location = models.CharField(max_length=20, default="", blank=True)

    def get_personal_info(self):
        return {'phone': self.phone_number, 'hours': self.office_hour,
                'office': self.office_number, 'building': self.office_location}

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class TA(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20, default="", null=True)
    office_hour = models.CharField(max_length=20, default="", null=True)
    office_number = models.CharField(max_length=20, default="", null=True)
    office_location = models.CharField(max_length=20, default="", null=True)

    def get_personal_info(self):
        return {'phone': self.phone_number, 'hours': self.office_hour,
                'office': self.office_number, 'building': self.office_location}

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Course(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True)
    department = models.CharField(max_length=20)
    course_num = models.CharField(max_length=3)

    def get_instructor(self):
        return self.instructor

    def get_instructor_personal_info(self):
        instructor = self.get_instructor()
        return instructor.get_personal_info()

    def __str__(self):
        return self.department + " " + self.course_num

class Section(models.Model):
    teachingAssistant = models.ForeignKey(TA, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(to="Course", on_delete=models.CASCADE)
    section_num = models.CharField(max_length=3)

    def get_TA(self):
        return self.teachingAssistant

    def get_TA_personal_info(self):
        teachingAssistant = self.get_TA()
        return teachingAssistant.get_personal_info()

    def __str__(self):
        return self.course.department + " " + self.course.course_num + "-" + self.section_num

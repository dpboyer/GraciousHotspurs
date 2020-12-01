from django.db import models


# Create your models here.

class MyUser(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name + self.password


#Simple Course Model with the option to add instructor which is represented by a MyUser object
class Course(models.Model):
    course_name = models.CharField(max_length=20)
    instructor = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name


#Section includes TAs and Course
class Section(models.Model):
    section_number = models.IntegerField(max_length=3)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    TAs = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.section_number)

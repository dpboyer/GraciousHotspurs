from django.db import models

# Create your models here.

class MyUser(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    #first_name = models.CharField(max_length=20)
    #last_name = models.CharField(max_length=20)
    #email = models.CharField(max_length=20)
    #phone_number = models.CharField(max_length=20)


    def __str__(self):
        return self.name + self.password

class Course(models.Model):
    department = models.CharField(max_length=20)
    course_num = models.CharField(max_length=3)


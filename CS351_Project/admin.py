from django.contrib import admin
from .models import Instructor, Course, Section

admin.site.register(Instructor)

admin.site.register(Course)
admin.site.register(Section)

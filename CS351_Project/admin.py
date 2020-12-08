from django.contrib import admin
from .models import Instructor, Course, Section,TA

admin.site.register(Instructor)

admin.site.register(Course)
admin.site.register(Section)
admin.site.register(TA)

"""GraciousHotspurs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from CS351_Project.views import Login, Home, AddUser, Courses, DelCourse, Sections, DelSection

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('', TemplateView.as_view(template_name='home.html'), name='home')
    path('', Login.as_view()),
    path('home/', Home.as_view()),
    path('home/adduser', AddUser.as_view()),
    #path('home/deleteuser', DeleteUser.as_view()),
    path('home/courses', Courses.as_view()),
    path('home/delcourse',DelCourse.as_view()),
    path('home/sections', Sections.as_view()),
    path('home/delsection', DelSection.as_view())
    #path('home/account', AddUser.as_view()),

]
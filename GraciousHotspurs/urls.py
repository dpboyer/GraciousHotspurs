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
from CS351_Project.views import Login, Home, AddUser, DelUser, Courses, DelCourse, Sections, DelSection, Account, Syllabus

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view()),
    path('home/', Home.as_view()),
    path('adduser/', AddUser.as_view()),
    path('deluser/', DelUser.as_view()),
    path('courses/', Courses.as_view()),
    path('delcourse/',DelCourse.as_view()),
    path('sections/', Sections.as_view()),
    path('delsection/', DelSection.as_view()),
    path('account/', Account.as_view()),
    path('syllabus/', Syllabus.as_view()),
    path('syllabus/<int:course>/<int:section>', Syllabus.as_view()),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('', TemplateView.as_view(template_name='home.html'), name='home')
]
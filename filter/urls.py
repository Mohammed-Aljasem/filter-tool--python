"""Task URL Configuration

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
from django.urls import path
from students.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', test),
    path('', student, name='student'),
    path('student/add', add_student, name='add'),
    path('student/delete/<int:id>', delete , name="delete"),
    path('edit/<int:id>', edit , name="edit"),
    path('update/<int:id>', update , name="update"),
    path('manage-students', manage_students , name="manage-students"),
    path('filter', filter , name="filter"),
]
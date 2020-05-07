"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views

app_name = "app1"

urlpatterns = [
    path('', views.home, name = "home"),
    path('login/', views.login_re, name = 'login'),
    path('logout/', views.logout_request, name  = "logout"),
    path('class/', views.cla, name = "class"),
    path('class/<nu_slug>%<se_slug>', views.cla_slug, name = "class_slug"),
    path('class_insert/', views.cla_in, name = "class_insert"),
    path('class_delete/', views.cla_del, name = "class_delete"),
    path('class/edit/<nu_slug>%<se_slug>', views.cla_edit_slug, name = "class_edit_slug"),
    path('class_all/', views.cla_all, name = "class_all"),
    path('teacher_insert/', views.teacher_in, name = "teacher_insert"),
    path('teacher_insert/add_class', views.add_class, name = "add_class"),
    path('teacher_insert/add_class/<slug>', views.add_class_slug, name = "add_class_slug"),
    path('teacher/', views.teacher, name = "teacher"),
    path('teacher/<slug>', views.teacher_slug, name = "teacher_slug"),
    path('teacher/edit/<slug>', views.teacher_up, name = "teacher_update"),
    path('teacher_delete/', views.teacher_del, name = "teacher_delete"),
    path('teacher_all/', views.teacher_all, name = "teacher_all"),
    path('user/', views.user_info, name = "user"),
]

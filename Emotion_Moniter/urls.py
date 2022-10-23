"""Emotion_Moniter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app01.views import account, admin

urlpatterns = [

    # 登录界面
    path('login/', account.login),
    path('login/student/', account.login_student),
    path('login/teacher/', account.login_teacher),
    path('login/admin/', account.login_admin),
    path('image/code/', account.image_code),

    # 管理员界面
    path('admin/home', admin.admin_home),
    path('list/admin/', admin.list_admin),
    path('add/admin/', admin.add_admin),
    path('edit/<int:nid>/admin/', admin.edit_admin),
    path('delete/<int:nid>/admin/', admin.delete_admin),
    path('reset/<int:nid>/admin/', admin.reset_admin),
    path('list/student/', admin.list_student),
    path('add/student/', admin.add_student),
    path('edit/<int:nid>/student/', admin.edit_student),
    path('delete/<int:nid>/student/', admin.delete_student),
    path('reset/<int:nid>/student/', admin.reset_student),
    path('list/teacher/', admin.list_teacher),
    path('add/teacher/', admin.add_teacher),
    path('edit/<int:nid>/teacher/', admin.edit_teacher),
    path('delete/<int:nid>/teacher/', admin.delete_teacher),
    path('reset/<int:nid>/teacher/', admin.reset_teacher),

]

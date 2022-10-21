from django.shortcuts import render,redirect,HttpResponse
from app01 import models
from app01.utils.form import LoginForm

def login(request):

    return render(request, 'choose_character.html')

def login_student(request):
    title = "学生登录"
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"title" : title, "form":form})

    form = LoginForm(data=request.POST)
    if form.is_valid():

        user_input_code = form.cleaned_data.pop("image_code")
        image_code = request.session.get("image_code", "")
        if image_code != user_input_code.upper():
            form.add_error("image_code", "验证码错误")
            return render(request, 'login.html', {"title": title, "form": form})

        sutdent_object = models.Student.objects.filter(**form.cleaned_data).first()

        if not sutdent_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {"title": title, "form": form})

        request.session["info"] = {"id": sutdent_object.id, "username": sutdent_object.username}
        request.session.set_expiry(60 * 60 * 27)
        return HttpResponse("登录成功")

    return render(request, 'login.html', {"title": title, "form": form})

def login_teacher(request):

    title = "老师登录"
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"title": title, "form": form})

    form = LoginForm(data=request.POST)
    if form.is_valid():

        user_input_code = form.cleaned_data.pop("image_code")
        image_code = request.session.get("image_code", "")
        if image_code != user_input_code.upper():
            form.add_error("image_code", "验证码错误")
            return render(request, 'login.html', {"title": title, "form": form})

        teacher_object = models.Teacher.objects.filter(**form.cleaned_data).first()

        if not teacher_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {"title": title, "form": form})

        request.session["info"] = {"id": teacher_object.id, "username": teacher_object.username}
        request.session.set_expiry(60 * 60 * 27)
        return HttpResponse("登录成功")

    return render(request, 'login.html', {"title": title, "form": form})

def login_admin(request):
    title = "管理员登录"
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"title": title, "form": form})

    form = LoginForm(data=request.POST)
    if form.is_valid():

        user_input_code = form.cleaned_data.pop("image_code")
        image_code = request.session.get("image_code", "")
        if image_code != user_input_code.upper():
            form.add_error("image_code", "验证码错误")
            return render(request, 'login.html', {"title": title, "form": form})

        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()

        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {"title": title, "form": form})

        request.session["info"] = {"id": admin_object.id, "username": admin_object.username}
        request.session.set_expiry(60 * 60 * 27)
        return HttpResponse("登录成功")

    return render(request, 'login.html', {"title": title, "form": form})
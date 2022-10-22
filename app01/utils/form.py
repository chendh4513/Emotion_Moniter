from django import forms
from app01.utils import encrypt , bootstrap

class LoginForm(bootstrap.BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "用户名"}),
        required=True
    )
    password = forms.CharField(
        label="用户名",widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "密码"})
    )

    image_code = forms.CharField(
        label="验证码",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "用户名"}),
        required=True
    )

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return encrypt.md5(pwd)


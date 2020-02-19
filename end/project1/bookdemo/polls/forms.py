from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """
        登录类
    """
    username = forms.CharField(max_length=10, min_length=3, label="用户名")
    password = forms.CharField(max_length=10, min_length=3, label="密码", widget=forms.PasswordInput)


class RegistForm(forms.ModelForm):
    """
    注册类
    """

    password2 = forms.CharField(min_length=3, max_length=20, label="重复密码", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password"]
        labels = {"username": "用户名", "password": "密码"}
        widgets = {
            "password": forms.PasswordInput()
        }
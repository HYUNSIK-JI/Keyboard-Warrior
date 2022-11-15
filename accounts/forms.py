from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CreateUser(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "press",
            "weight",
            "array",
            "sound",
            "connect",
            "image",
        ]
        labels = {
            "username": "아이디",
            "email": "이메일 ",
            "press": "키압",
            "weight": "무게",
            "array": "배열",
            "sound": "소리",
            "connect": "연결",
        }


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "email",
            "press",
            "weight",
            "array",
            "sound",
            "connect",
            "image",
        ]
        labels = {
            "username": "아이디",
            "email": "이메일 ",
            "press": "키압",
            "first_name": "이름",
            "last_name": "성",
            "weight": "무게",
            "array": "배열",
            "sound": "소리",
            "connect": "연결",
        }


class SocialUserForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = [
            "press",
            "weight",
            "array",
            "sound",
            "connect",
        ]
        labels = {
            "press": "키압",
            "weight": "무게",
            "array": "배열",
            "sound": "소리",
            "connect": "연결",
        }

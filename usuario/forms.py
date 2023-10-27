from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models.usuario import Usuario


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ("email",)

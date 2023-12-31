from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group

from ..managers import CustomUserManager

class Usuario(AbstractUser):
    username = None
    email = models.EmailField(_("e-mail address"), unique=True)
    cpf = models.CharField(_("CPF"), max_length=11, blank=True, null=True)
    telefone = models.CharField(_("Phone"), max_length=11, blank=True, null=True)
    data_nascimento = models.DateField(
        _("Birth Date"), auto_now=False, auto_now_add=False, blank=True, null=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"
    objects = CustomUserManager()

    # imagem_perfil = models.ForeignKey(
    #     "uploader.Image",
    #     verbose_name=_("Profile Image"),
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    # )

    imagem_perfil = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.email
    def save(self, *args, **kwargs):
        created = not self.pk  # Check if the user is being created for the first time
        super().save(*args, **kwargs)
        # If the user is being created, assign them to the "cliente" group
        if created:
            compradores_group, _ = Group.objects.get_or_create(name="compradores")
            self.groups.add(compradores_group)
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-date_joined"]
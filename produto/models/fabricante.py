from django.db import models


class Fabricante(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    site = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome

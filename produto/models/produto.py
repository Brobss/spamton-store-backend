from django.db import models

from .categoria import Categoria
from .fabricante import Fabricante


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=0)
    fabricante = models.ForeignKey(
        Fabricante, null=True, blank=True, on_delete=models.CASCADE
    )
    promo = models.BooleanField(default=False)
    precoPromo = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="thumbnails/", blank=True, null=True)
    imagens = models.ManyToManyField("uploader.Image", blank=True)

    def __str__(self):
        return self.nome

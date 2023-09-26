from django.db import models

from produto.models.categoria import Categoria
from produto.models.fabricante import Fabricante


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=0)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="produtos"
    )
    fabricante = models.ForeignKey(
        Fabricante, on_delete=models.PROTECT, related_name="produtos"
    )
    promo = models.BooleanField(default=False)
    precoPromo = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    thumbnail = models.ForeignKey(
        "uploader.Image",
        on_delete=models.CASCADE,
        related_name="thumbnail",
        blank=True,
        null=True,
    )
    imagens = models.ManyToManyField("uploader.Image", blank=True)

    def __str__(self):
        return self.nome

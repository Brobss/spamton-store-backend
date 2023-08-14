""" from django.db import models

from .produto import Produto

from PIL import Image


class Imagem(models.Model):
    produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE, related_name="imagens"
    )
    imagem = models.ImageField(upload_to="imagens/", blank=True, null=True)

    def salvar(self, *args, **kwargs):
        super(Imagem, self).save(*args, **kwargs)
        img = Image.open(self.imagem.path)
        if img.height > 1125 or img.width > 1125:
            img.thumbnail((1125, 1125))
        img.save(self.imagem.path, quality=70, optimize=True)

    def __str__(self):
        return self.imagem.name

    class Meta:
        verbose_name_plural = "Imagens" """

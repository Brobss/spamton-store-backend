from django.db import models

from PIL import Image


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
class Fabricante(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="fabricantes/", blank=True, null=True)
    site = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=0)
    fabricante = models.ForeignKey(Fabricante,null=True, blank=True, on_delete=models.CASCADE)
    promo = models.BooleanField(default=False)
    precoPromo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="thumbnails/", blank=True, null=True)

    def __str__(self):
        return self.nome


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
        verbose_name_plural = "Imagens"


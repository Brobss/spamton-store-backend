from django.contrib import admin

from .models import Categoria, Produto, Fabricante
from uploader.models import Image


class ImagemAdmin(admin.StackedInline):
    model = Image


class ProdutoAdmin(admin.ModelAdmin):
    inlines = [ImagemAdmin]

    class Meta:
        model = Produto


class FabricanteAdmin(admin.ModelAdmin):
    class Meta:
        model = Fabricante


admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
""" admin.site.register(Image) """
admin.site.register(Fabricante, FabricanteAdmin)

from django.contrib import admin

from .models import Categoria, Produto, Fabricante
from uploader.models import Image
from produto.models import Compra, ItensCompra


class ImagemAdmin(admin.StackedInline):
    model = Image


class ProdutoAdmin(admin.ModelAdmin):
    class Meta:
        model = Produto


class FabricanteAdmin(admin.ModelAdmin):
    class Meta:
        model = Fabricante


admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Fabricante, FabricanteAdmin)

admin.site.register(Compra)


class ItensCompraInline(admin.TabularInline):
    model = ItensCompra


# @admin.register(Compra)
# class CompraAdmin(admin.ModelAdmin):
#     inlines = [ItensCompraInline]

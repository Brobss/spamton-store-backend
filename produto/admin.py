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

class ItensCompraInline(admin.TabularInline):
    model = ItensCompra
    

class CompraAdmin(admin.ModelAdmin):
    inlines = [ItensCompraInline]

admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Compra, CompraAdmin)
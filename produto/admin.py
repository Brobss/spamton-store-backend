from django.contrib import admin

from .models import Categoria, Produto, Imagem, Fabricante


class ImagemAdmin(admin.StackedInline):
    model = Imagem


class ProdutoAdmin(admin.ModelAdmin):
    inlines = [ImagemAdmin]

    class Meta:
        model = Produto

class FabricanteAdmin(admin.ModelAdmin):
    class Meta:
        model = Fabricante


admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Imagem)
admin.site.register(Fabricante, FabricanteAdmin)

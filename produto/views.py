from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from produto.models import Categoria, Produto, Imagem, Fabricante
from produto.serializers import CategoriaSerializer, ProdutoSerializer, ProdutoListSerializer, ImagemSerializer, FabricanteSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ProdutoListSerializer
        return ProdutoSerializer
    
class ImagemViewSet(ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer

class FabricanteViewSet(ModelViewSet):
    queryset = Fabricante.objects.all()
    serializer_class = FabricanteSerializer



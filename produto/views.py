from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from produto.models import Categoria, Produto, Imagem
from produto.serializers import CategoriaSerializer, ProdutoSerializer, ImagemSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
class ImagemViewSet(ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer

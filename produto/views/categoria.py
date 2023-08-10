from rest_framework.viewsets import ModelViewSet

from produto.models import Categoria
from produto.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

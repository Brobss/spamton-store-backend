from rest_framework.viewsets import ModelViewSet

from produto.models import Produto
from produto.serializers import ProdutoSerializer, ProdutoListSerializer, ProdutoDetailSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ProdutoListSerializer
        elif self.action == "retrieve":
            return ProdutoDetailSerializer
        return ProdutoSerializer
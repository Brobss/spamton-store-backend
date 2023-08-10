from rest_framework.viewsets import ModelViewSet

from produto.models import Produto
from produto.serializers import ProdutoSerializer, ProdutoListSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ProdutoListSerializer
        return ProdutoSerializer

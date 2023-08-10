from rest_framework.serializers import ModelSerializer

from produto.models import Produto


class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"


class ProdutoListSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1

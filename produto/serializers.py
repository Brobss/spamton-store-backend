from rest_framework.serializers import ModelSerializer

from produto.models import Categoria, Produto, Imagem, Fabricante


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class ImagemSerializer(ModelSerializer):
    class Meta:
        model = Imagem
        fields = "__all__"

class FabricanteSerializer(ModelSerializer):
    class Meta:
        model = Fabricante
        fields = "__all__"

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"

class ProdutoListSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1
from rest_framework.serializers import ModelSerializer

from produto.models import Categoria, Produto, Imagem


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        
class ImagemSerializer(ModelSerializer):
    class Meta:
        model = Imagem
        fields = "__all__"

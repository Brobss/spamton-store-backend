from rest_framework.serializers import ModelSerializer, SlugRelatedField

from produto.models import Produto

from uploader.models import Image
from uploader.serializers import ImageSerializer


class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"




class ProdutoListSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)

    class Meta:
        model = Produto
        fields = "__all__"


class ProdutoListSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1

from rest_framework.serializers import ModelSerializer, SlugRelatedField

from produto.models import Produto

from uploader.models import Image
from uploader.serializers import ImageSerializer


class ProdutoSerializer(ModelSerializer):
    imagens_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    imagens = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1


class ProdutoListSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = ["id", "nome", "thumbnail","preco","promo","precoPromo"]

class ProdutoDetailSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 2

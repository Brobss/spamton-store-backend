from rest_framework.serializers import ModelSerializer, SlugRelatedField

from produto.models import Produto

from uploader.models import Image
from uploader.serializers import ImageSerializer


class ProdutoSerializer(ModelSerializer):
    imagens_attachment_key = SlugRelatedField(
        source="imagens",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    imagens = ImageSerializer(required=False, read_only=True)

    thumb_attachment_key = SlugRelatedField(
        source="thumbnail",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    thumbnail = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Produto
        fields = "__all__"


class ProdutoListSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = ["id", "nome", "thumbnail", "preco", "promo", "precoPromo"]
        depth = 1


class ProdutoDetailSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 2

from rest_framework.serializers import ModelSerializer

from produto.models import Imagem


class ImagemSerializer(ModelSerializer):
    class Meta:
        model = Imagem
        fields = "__all__"

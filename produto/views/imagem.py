""" from rest_framework.viewsets import ModelViewSet

from produto.models import Imagem
from produto.serializers import ImagemSerializer


class ImagemViewSet(ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer
 """
from rest_framework.viewsets import ModelViewSet

from produto.models import Fabricante
from produto.serializers import FabricanteSerializer


class FabricanteViewSet(ModelViewSet):
    queryset = Fabricante.objects.all()
    serializer_class = FabricanteSerializer

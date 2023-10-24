from rest_framework.viewsets import ModelViewSet
from .permissions import AllowAnonymousPost

from .models import Usuario
from .serializers import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAnonymousPost]
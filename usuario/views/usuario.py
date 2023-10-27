from rest_framework.viewsets import ModelViewSet
from usuario.permissions import AllowAnonymousPost

from usuario.models.usuario import Usuario
from usuario.serializers.usuario import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAnonymousPost]
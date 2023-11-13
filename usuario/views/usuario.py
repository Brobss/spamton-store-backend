from rest_framework.viewsets import ModelViewSet
from usuario.permissions import AllowAnonymousPost

from usuario.models.usuario import Usuario
from usuario.serializers.usuario import UsuarioSerializer, UsuarioReadSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [AllowAnonymousPost]
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UsuarioReadSerializer
        return UsuarioSerializer
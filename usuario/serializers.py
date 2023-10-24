from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import Usuario


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

    def create(self, validated_data):
        return Usuario.objects.create_user(**validated_data)

    
    # def create(self, validated_data):
    #     user = Usuario
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user
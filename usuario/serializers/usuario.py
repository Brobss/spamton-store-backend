from rest_framework.serializers import ModelSerializer, SlugRelatedField
from uploader.models import Image
from uploader.serializers import ImageSerializer
from ..models.usuario import Usuario


class UsuarioSerializer(ModelSerializer):
    # imagem_perfil_attachment_key = SlugRelatedField(
    #     source="imagem_perfil",
    #     queryset=Image.objects.all(),
    #     slug_field="attachment_key",
    #     required=False,
    #     write_only=True,
    # )
    # imagem_perfil = ImageSerializer(required=False, read_only=True)

    def create(self, validated_data):
        return Usuario.objects.create_user(**validated_data)

    class Meta:
        model = Usuario
        fields = ("email", "first_name", "last_name", "password", "imagem_perfil", "telefone", "cpf", "data_nascimento","id")


    
    # def create(self, validated_data):
    #     user = Usuario
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user
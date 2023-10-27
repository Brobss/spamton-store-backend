from rest_framework.serializers import ModelSerializer, SlugRelatedField
from uploader.models import Image
from uploader.serializers import ImageSerializer
from ..models.usuario import Usuario


class UsuarioSerializer(ModelSerializer):
    # foto_attachment_key = SlugRelatedField(
    #     source="foto",
    #     queryset=Image.objects.all(),
    #     slug_field="attachment_key",
    #     required=False,
    #     write_only=True,
    # )
    # foto = ImageSerializer(required=False, read_only=True)

    def create(self, validated_data):
        return Usuario.objects.create_user(**validated_data)

    class Meta:
        model = Usuario
        fields = "__all__"


    
    # def create(self, validated_data):
    #     user = Usuario
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user
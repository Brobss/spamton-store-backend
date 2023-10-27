# Generated by Django 4.2.6 on 2023-10-27 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("uploader", "0003_remove_image_produto"),
        ("usuario", "0006_delete_salvacao"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usuario",
            name="imagem_perfil",
        ),
        migrations.AddField(
            model_name="usuario",
            name="foto",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="uploader.image",
                verbose_name="Profile Image",
            ),
        ),
    ]
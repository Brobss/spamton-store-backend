# Generated by Django 4.2.3 on 2023-08-12 18:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("produto", "0005_produto_fabricante"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Imagem",
        ),
    ]
# Generated by Django 4.2.4 on 2023-09-26 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0014_produto_nome21'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='nome21',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='produto.categoria'),
        ),
    ]

from django.db import models

from usuario.models.usuario import Usuario
from . import Produto


class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = (
            1,
            "Carrinho",
        )
        REALIZADO = (
            2,
            "Realizado",
        )
        PAGO = (
            3,
            "Pago",
        )
        ENTREGUE = (
            4,
            "Entregue",
        )

    usuario = models.ForeignKey(
        Usuario, on_delete=models.PROTECT, related_name="compras"
    )
    status = models.IntegerField(
        choices=StatusCompra.choices, default=StatusCompra.CARRINHO
    )

    @property
    def total(self):
        # total = 0
        # for item in self.itens.all():
        #     total += item.produto.preco * item.quantidade
        # return total
        return sum(item.produto.preco * item.quantidade for item in self.itens.all())


class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField(default=1)

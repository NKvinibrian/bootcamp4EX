from django.db import models

# Create your models here.
class Cliente(models.Model):
    cpf = models.CharField(max_length=11, null=True)
    nome = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'cliente'

class Produtos(models.Model):
    nome = models.CharField(max_length=100, null=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    estoque = models.IntegerField(null=True)
    imagem = models.ImageField(upload_to='produtos_img', null=True, blank=True)
    descricao = models.TextField(null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = 'produtos_ecom'

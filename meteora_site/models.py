from django.db import models
# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.CharField(max_length=500, blank=False, null=False)
    criado_em = models.DateTimeField(auto_created=True)
    atualizado_em = models.DateTimeField(auto_now=True)


class Produto(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.CharField(max_length=1000, blank=False, null=False)
    preco = models.DecimalField(blank=False, null=False, max_digits=1000, decimal_places=2) 
    quantidade_estoque = models.IntegerField(blank=False, null=False)
    categoria = models.ForeignKey(
        "Categoria", on_delete=models.DO_NOTHING
    )
    image = models.ImageField(
        null=True, 
        upload_to="assets/image/%M/%d",
        default=None
    )
    criado_em = models.DateTimeField(auto_created=True)
    atualizado_em = models.DateTimeField(auto_now=True)


from rest_framework import serializers
from meteora_site.models import Categoria, Produto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        models = Categoria
        fields = "__all__"

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        models = Produto
        fields = "__all__"

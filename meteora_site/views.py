from meteora_site.models import Categoria, Produto
from rest_framework import viewsets
from meteora_site.serializers import CategoriaSerializer, ProdutoSerializer
from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['categoria', "nome", "preco"] 
    ordering = ["preco"]
    permission_classes = [IsAuthenticatedOrReadOnly]


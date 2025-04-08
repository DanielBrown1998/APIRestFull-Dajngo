from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from meteora_site.views import CategoriaViewSet, ProdutoViewSet

route = routers.DefaultRouter()
route.register(r"categorias", CategoriaViewSet)
route.register(r"produtos", ProdutoViewSet)

urlpatterns = [
    path("", include(route.urls)),
]

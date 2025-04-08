from django.contrib import admin

from meteora_site.models import Categoria, Produto

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    field = [
        "nome",
    ]
    ordering = ["nome"]
    search_fields = ["nome"]

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    field = [
        "nome",
        "categoria"
    ]
    ordering = ["nome", "categoria"]
    search_fields = ["nome"]

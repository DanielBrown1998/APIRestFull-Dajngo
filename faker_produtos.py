from django.conf import settings 
import os, django, random
from faker import Faker
import random
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from meteora_site.models import Categoria, Produto

dados = [
    ('vestuario', 'roupas no geral'),
    ('calcados', 'tenis, sapatos, chinelos etc.'),
    ('acessorio', 'brincos, relogios, pulseiras etc.'),
]

create = datetime.now()

def criando_pessoas(quantidade_de_produtos):
    Produto.objects.all().delete()
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_produtos):
        nome = fake.name()
        descricao = fake.random_letter()
        cat = random.choice(dados)
        categoria = Categoria.objects.get(
            nome=cat[0]
        )
        preco = fake.random_number(fix_len=True, digits=2)
        quantidade_prod=random.randint(1,50)
        p = Produto(nome=nome, descricao=descricao, preco = preco, categoria=categoria, quantidade_estoque=quantidade_prod, criado_em=create,  atualizado_em=create)
        p.save()

def criar_cursos():
    Categoria.objects.all().delete()
    fake = Faker('pt_BR')
    Faker.seed(10)
    for codigo, descricao in dados:
        c = Categoria(nome=codigo, descricao=descricao, criado_em=create,  atualizado_em=create)
        c.save()

criar_cursos()
criando_pessoas(50)
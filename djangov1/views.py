from rest_framework import viewsets
from djangov1.models import Produto, Categoria
from djangov1.serializer import ProdutoSerializer, CategoriaSerializer

class ProdutosViewSet(viewsets.ModelViewSet):
    """EXIBIR TODOS OS PRODUTOS"""
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class CategoriasViewSet(viewsets.ModelViewSet):
    """EXIBIR TODAS AS CATEGORIAS"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
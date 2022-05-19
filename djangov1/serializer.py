from rest_framework import serializers
from djangov1.models import Produto, Categoria

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'preco', 'descricao', 'categoria', 'data_criacao']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'



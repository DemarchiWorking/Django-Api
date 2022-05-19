from django.contrib import admin
from django.urls import path, include
from djangov1.views import ProdutosViewSet, CategoriasViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('produtos', ProdutosViewSet, basename='Produtos')
router.register('categorias', CategoriasViewSet, basename='Categorias')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

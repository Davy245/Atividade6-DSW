from django.urls import path
from .views import *

urlpatterns = [
    path('', listarDiscos, name='listar_discos'),
    path('detalhes/<int:pk>', detalheDisco, name='detalhe_disco'),
]
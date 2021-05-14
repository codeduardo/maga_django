from django.urls import path
from Producto import views

urlpatterns= [
    path('producto/',views.listaP, name="Productos"),
    path('producto/categoria/<int:categoria_id>',views.categoria, name="Categoria"),
    path('pedidos/',views.pedidos, name="Pedidos"),
    path('pedidos/search',views.listaP_post, name="Buscador"),
]
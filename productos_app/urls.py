from django.urls import path
from . import views

urlpatterns = [
    # Es la pagina principal
    path('', views.list_products, name='list_products'), 
    # Es la pagina donde se agregan los productos
    path('agregar/', views.add_product, name='add_product'), 
    # Es la orden para eliminar un producto
    path('eliminar/<int:pk>/', views.delete_product, name='delete_product'), 
    # Te redirige a los detalles del producto
    path('detalle/<int:id>/', views.detail_product, name='detail_product'), 
    # Conduce a la pagina para agregar caracteristicas
    path('caracteristica/agregar/<int:producto_id>/', views.add_caracteristica, name='add_caracteristica'), 
    # Pagina para editar las caracteristicas
    path('caracteristica/editar/<int:caracteristica_id>/', views.edit_caracteristica, name='edit_caracteristica'),
    # Eliminar caracteristicas
    path('caracteristica/eliminar/<int:id>/', views.delete_caracteristica, name='delete_caracteristica')
]
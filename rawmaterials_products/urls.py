from django.urls import path
from .views import add, getAll, getById, update, delete,getByProductId

urlpatterns = [
    path('add/', add, name='add_raw_material_product'),
    path('getall/', getAll, name='get_all_raw_material_products'),
    path('getbyid/<int:id>/', getById, name='get_raw_material_product_by_id'),
    path('getbyproductid/<int:product_id>/', getByProductId, name='get_raw_material_products_by_product_id'),
    path('update/<int:product_id>/', update, name='update_raw_material_product'),
    path('delete/<int:product_id>/', delete, name='delete_raw_material_product'),
]

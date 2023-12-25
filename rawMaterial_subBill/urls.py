from django.urls import path
from rawMaterial_subBill import views

urlpatterns = [
    path('add/',views.add),
    path('getall/',views.getAll),
    path('get/<int:id>/id/',views.getById),
    path('<int:id>/edit/',views.update),
    path('<int:id>/delete/',views.delete)
]

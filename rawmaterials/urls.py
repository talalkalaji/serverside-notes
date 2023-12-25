from django.urls import path
from rawmaterials import views

urlpatterns = [
    path('add/',views.add),
    path('getall/',views.getall),
    path('get/<int:id>/id/',views.getById),
    path('get/<str:name>/name/',views.getname),
    path('<int:id>/edit/',views.update),
    path('delete/<int:id>/',views.deleteR),
    
]

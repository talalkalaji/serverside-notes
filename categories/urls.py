from django.urls import path
from categories import views

urlpatterns = [
    path('add/',views.add),
    path('getall/',views.getall),
    path('get/<int:id>/id/',views.getById),
    path('get/<str:name>/name/',views.getname),
    path('<int:id>/edit/',views.update),
    path('<int:id>/delete/',views.delete)
]

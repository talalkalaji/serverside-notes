from django.urls import path
from sup_bill import views

urlpatterns = [
    path('add/',views.add),
    path('getall/',views.getall),
    path('get/<int:id>/id/',views.getid),
    path('<int:id>/edit/',views.update),
    path('<int:id>/delete/',views.delete)
]

# your_app/views.py
from django.shortcuts import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SupplierSerializer
from .models import Supplier

@api_view(['GET'])
def getall(request):
    suppliers = Supplier.objects.all()
    supplier_serializer = SupplierSerializer(suppliers, many=True)
    return Response(supplier_serializer.data, headers={'Access-Control-Allow-Origin': '*'})

@api_view(['POST'])
def add(request):
    supplier_serializer = SupplierSerializer(data=request.data)
    if supplier_serializer.is_valid():
        supplier_serializer.save()
        return Response(supplier_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(supplier_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getid(request, id):
    try:
        supplier = Supplier.objects.get(id=id)
        supplier_serializer = SupplierSerializer(supplier)
        return Response(supplier_serializer.data)
    except Supplier.DoesNotExist:
        return HttpResponse("Supplier does not exist", status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update(request, id):
    try:
        supplier = Supplier.objects.get(pk=id)
    except Supplier.DoesNotExist:
        return Response({'error': 'Supplier not found'}, status=status.HTTP_404_NOT_FOUND)

    supplier_serializer = SupplierSerializer(supplier, data=request.data)
    if supplier_serializer.is_valid():
        supplier_serializer.save()
        return Response({'status': 'Updated successfully'}, status=status.HTTP_200_OK)
    else:
        return Response(supplier_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete(request, id):
    try:
        supplier = Supplier.objects.get(pk=id)
    except Supplier.DoesNotExist:
        return Response({'error': 'Supplier not found'}, status=status.HTTP_404_NOT_FOUND)

    supplier.delete()
    return Response({'status': 'Supplier deleted successfully'}, status=status.HTTP_200_OK)

from django.shortcuts import render, HttpResponse
from .models import BillSupplier
from .serializers import BillSupplierUpdateSerializer, BillSupplierListSerializer, BillSupplierSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

@api_view(['POST'])
def add(request):
    bill_supplier_serializer = BillSupplierSerializer(data=request.data)
    if bill_supplier_serializer.is_valid():
        bill_supplier_serializer.save()
        return Response(bill_supplier_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(bill_supplier_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getall(request):
    bill_suppliers = BillSupplier.objects.all()
    bill_supplier_serializer = BillSupplierSerializer(bill_suppliers, many=True)
    return Response(bill_supplier_serializer.data, headers={'Access-Control-Allow-Origin': '*'})

@api_view(['GET'])
def getid(request, id):
    try:
        bill_supplier = BillSupplier.objects.get(id=id)
        bill_supplier_serializer = BillSupplierSerializer(bill_supplier)
        return Response(bill_supplier_serializer.data)
    except BillSupplier.DoesNotExist:
        return HttpResponse("Not Exist", status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update(request, id):
    try:
        bill_supplier = BillSupplier.objects.get(id=id)
        bill_supplier_update_serializer = BillSupplierUpdateSerializer(instance=bill_supplier, data=request.data)

        if bill_supplier_update_serializer.is_valid():
            bill_supplier_update_serializer.save()
            result = {'status': 'Done'}
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(bill_supplier_update_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except BillSupplier.DoesNotExist:
        return Response({'status': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete(request, id):
    try:
        bill_supplier = BillSupplier.objects.get(id=id)
    except BillSupplier.DoesNotExist:
        return Response({'error': 'BillSupplier not found'}, status=status.HTTP_404_NOT_FOUND)

    bill_supplier.delete()
    result = {
        'status': 'deleted',
        'id': id
    }
    return Response(result, status=status.HTTP_200_OK)

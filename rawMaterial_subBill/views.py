from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import RawMaterialSupplierBill
from .serializers import RawMaterialSupplierBillSerializer, RawMaterialSupplierBillUpdateSerializer

@api_view(['POST'])
def add(request):
    rawSupp = RawMaterialSupplierBillSerializer(data=request.data, many=True)
    if rawSupp.is_valid():
        rawSupp.save()
        return Response(rawSupp.data, status=status.HTTP_201_CREATED)
    return Response(rawSupp.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getAll(request):
    rawSupps = RawMaterialSupplierBill.objects.all()
    rawSuppsSerializer = RawMaterialSupplierBillSerializer(rawSupps, many=True)
    return Response(rawSuppsSerializer.data)

@api_view(['GET'])
def getById(request, id):
    rawSuppBill = get_object_or_404(RawMaterialSupplierBill, id=id)
    rawSuppBillSerializer = RawMaterialSupplierBillSerializer(rawSuppBill)
    return Response(rawSuppBillSerializer.data)


@api_view(['PUT'])
def update(request, id):
    try:
        rawMaterialSupplierBill = RawMaterialSupplierBill.objects.get(id=id)
    except RawMaterialSupplierBill.DoesNotExist:
        return Response({'status': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

    rawMaterialSupplierBillUpdateSerializer = RawMaterialSupplierBillUpdateSerializer(instance=rawMaterialSupplierBill, data=request.data)

    if rawMaterialSupplierBillUpdateSerializer.is_valid():
        rawMaterialSupplierBillUpdateSerializer.save()
        return Response({'status': 'Done'}, status=status.HTTP_200_OK)
    else:
        return Response(rawMaterialSupplierBillUpdateSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete(request, id):
    rawSuppBill = get_object_or_404(RawMaterialSupplierBill, id=id)
    rawMaterial = rawSuppBill.rawMaterial
    rawMaterial.quantity -= rawSuppBill.quantity
    rawMaterial.save()
    rawSuppBill.delete()
    return Response({'status': 'deleted', 'id': id}, status=status.HTTP_200_OK)

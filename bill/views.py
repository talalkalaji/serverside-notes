from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Bill
from .serializers import BillSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def add(request):
    bill = BillSerializer(data=request.data)
    if bill.is_valid():
        bill.save()
        return Response(bill.data, status=status.HTTP_201_CREATED)
    else:
        return Response(bill.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getAll(request):
    bills = Bill.objects.all()
    billSerializer = BillSerializer(bills, many=True)
    return Response(billSerializer.data)

@api_view(['GET'])
def getById(request, id):
    bill = get_object_or_404(Bill, id=id)
    billSerializer = BillSerializer(bill)
    return Response(billSerializer.data)

@api_view(['PUT'])
def update(request, id): 
    data = request.data
    bill = Bill.objects.get(pk = id)
    billSerializer = BillSerializer(bill, data)
    if billSerializer.is_valid():
        billSerializer.save()
        result = {
                'status' : 'Done'
            }
        return Response(result, status = status.HTTP_202_ACCEPTED)

@api_view(['DELETE'])
def delete(request, id):
    bill = Bill.objects.get(pk = id)
    bill.delete()
    return Response({"status": "deleted", "id": id})

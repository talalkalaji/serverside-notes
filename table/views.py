from django.shortcuts import render, HttpResponse
from .models import Table
from .serializers import TableSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def add(request):
    tableSerializer = TableSerializer(data=request.data)
    if tableSerializer.is_valid():
        tableSerializer.save()
        return Response(tableSerializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(tableSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getAll(request):
    tables = Table.objects.all()
    tableSerializer = TableSerializer(tables, many=True)
    return Response(tableSerializer.data)

@api_view(['GET'])
def getById(request, table_number):
    try:
        table = Table.objects.get(table_number=table_number)
        tableSerializer = TableSerializer(table)
        return Response(tableSerializer.data)
    except Table.DoesNotExist:
        return Response({"error": "Table not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update(request, table_number):
    try:
        table = Table.objects.get(table_number=table_number)
        tableSerializer = TableSerializer(table, data=request.data)
        if tableSerializer.is_valid():
            tableSerializer.save()
            return Response(tableSerializer.data)
        else:
            return Response(tableSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Table.DoesNotExist:
        return Response({"error": "Table not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete(request, table_number):
    try:
        table = Table.objects.get(table_number=table_number)
        table.delete()
        return Response({"status": "deleted", "table_number": table_number})
    except Table.DoesNotExist:
        return Response({"error": "Table not found"}, status=status.HTTP_404_NOT_FOUND)

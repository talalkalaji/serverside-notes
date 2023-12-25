from django.shortcuts import render , HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from products.serializers import ProductSerializer
from products.models import Product

@api_view(['GET'])
def getall(request):
    products = Product.objects.all()
    productSerializer = ProductSerializer(products, many=True)
    return Response(productSerializer.data, headers={'Access-Control-Allow-Origin': '*'})


@api_view(['POST'])
def add(request):
    productSerializer = ProductSerializer(data=request.data)
    if productSerializer.is_valid():
        productSerializer.save()
        return Response(productSerializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(productSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getid(request, id):
    try:
        product = Product.objects.get(id=id)
        productSerializer = ProductSerializer(product)
        return Response(productSerializer.data)
    except:
        return HttpResponse("Not Exist")

@api_view(['GET'])
def getname(request, name):
    try:
        product = Product.objects.get(name=name)
        productSerializer = ProductSerializer(product)
        return Response(productSerializer.data)
    except Product.DoesNotExist:
        result = {
            'status': 'Product not found'
        }
        return Response(result, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update(request, id): 
    data = request.data
    product = Product.objects.get(pk = id)
    productSerializer = ProductSerializer(product, data)
    if productSerializer.is_valid():
        productSerializer.save()
        result = {
                'status' : 'Done'
            }
        return Response(result, status = status.HTTP_202_ACCEPTED)
    else:
        result = {
            'status':'Error'
            }    
        return Response(result, status = status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def delete(request, id):
    try:
        product = Product.objects.get(pk=id)
    except ObjectDoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    if product.delete():
        result = {
            'status': 'Product deleted',
            'id': id
        }
        return Response(result, status=status.HTTP_200_OK)
    else:
        result = {
            'error': 'Error in deleting product'
        }
        return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

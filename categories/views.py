from django.shortcuts import render,HttpResponse
from categories.models import Category
from categories.serializers import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def add(request):
    category = CategorySerializer(data = request.data)
    if category.is_valid():
        category.save()
        return Response(category.data,status = status.HTTP_201_CREATED)
    else:
        return Response(category.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getall(request):
    categories = Category.objects.all()
    categoriesSerializers = CategorySerializer(categories, many=True)
    return Response(categoriesSerializers.data, headers={'Access-Control-Allow-Origin': '*'})

    
@api_view(['GET'])
def getById (request , id):
    try:
        category = Category.objects.get(id = id)
        
        categorySerializer = CategorySerializer(category)
        
        return Response(categorySerializer.data)
    except:
        return HttpResponse("Not Exist")
    

@api_view(['GET'])
def getname(request, name):
    try:
        category = Category.objects.get(name=name)
        categorySerializer = CategorySerializer(category)
        return Response(categorySerializer.data)
    except Category.DoesNotExist:
        result = {
            'status': 'Category not found'
        }
        return Response(result, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update(request, id): 
    data = request.data
    category = Category.objects.get(pk = id)
    categorySerializer = CategorySerializer(category, data)
    if categorySerializer.is_valid():
        categorySerializer.save()
        result = {
                'status' : 'Done'
            }
        return Response(result, status = status.HTTP_202_ACCEPTED)

@api_view(['DELETE'])
def delete(request, id):
    try:
        category = Category.objects.get(pk=id)
    except ObjectDoesNotExist:
        return Response({'error': 'category not found'}, status=status.HTTP_404_NOT_FOUND)       
    if category.delete():
        result = {
            'status': 'Category deleted',
            'id': id
        }
        return Response(result, status=status.HTTP_200_OK)
    else:
        result = {
            'error': 'Error in deleting category'
        }
        return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    


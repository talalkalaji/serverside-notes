from django.shortcuts import render,HttpResponse
from rawmaterials.models import RawMaterial
from rawmaterials.serializers import RawMaterialSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def add(request):
    rawMaterial = RawMaterialSerializer(data = request.data)
    if rawMaterial.is_valid():
        rawMaterial.save()
        return Response(rawMaterial.data,status = status.HTTP_201_CREATED)
    else:
        return Response(rawMaterial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getall(request):
    rawMaterials = RawMaterial.objects.all()
    rawMaterialsSerializer = RawMaterialSerializer(rawMaterials, many=True)
    return Response(rawMaterialsSerializer.data, headers={'Access-Control-Allow-Origin': '*'})
    
@api_view(['GET'])
def getById (request , id):
    try:
        rawMaterial = RawMaterial.objects.get(id = id)        
        rawMaterialSerializer = RawMaterialSerializer(rawMaterial)        
        return Response(rawMaterialSerializer.data)
    except:
        return HttpResponse("Not Exist")
    

@api_view(['GET'])
def getname(request, name):
    try:
        rawMaterial = RawMaterial.objects.get(name=name)
        rawMaterialSerializer = RawMaterialSerializer(rawMaterial)
        return Response(rawMaterialSerializer.data)
    except RawMaterial.DoesNotExist:
        result = {
            'status': 'Category not found'
        }
        return Response(result, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update(request, id): 
    data = request.data
    rawMaterial = RawMaterial.objects.get(pk = id)
    rawMaterialSerializer = RawMaterialSerializer(rawMaterial, data)
    if rawMaterialSerializer.is_valid():
        rawMaterialSerializer.save()
        result = {
                'status' : 'Done'
            }
        return Response(result, status = status.HTTP_202_ACCEPTED)
@api_view(['DELETE'])
def deleteR(request, id):
    print(request.method)
    try:
        rawMaterial = RawMaterial.objects.get(pk=id)
    except ObjectDoesNotExist:
        return Response({'error': 'rawMaterial not found'}, status=status.HTTP_404_NOT_FOUND)       
    if rawMaterial.delete():
        result = {
            'status': 'deleted',
            'id': id
        }
        return Response(result, status=status.HTTP_200_OK)
    else:
        result = {
            'error': 'Error in deleting rawMaterial'
        }
        return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from django.shortcuts import render,HttpResponse
from rawmaterials_products.models import RawMaterialProduct
from .serializers import RawMaterialProductUpdateSerializer,RawMaterialProductListSerializer,RawMaterialProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def add(request):
    rawMaterialProduct = RawMaterialProductSerializer(data = request.data,many=True)
    if rawMaterialProduct.is_valid():
        rawMaterialProduct.save()
        return Response(rawMaterialProduct.data,status = status.HTTP_201_CREATED)
    else:
        return Response(rawMaterialProduct.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getAll(request):
    rawMaterialsProduct = RawMaterialProduct.objects.all()
    rawMaterialsProductSerializer = RawMaterialProductSerializer(rawMaterialsProduct, many=True)
    return Response(rawMaterialsProductSerializer.data, headers={'Access-Control-Allow-Origin': '*'})
    
@api_view(['GET'])
def getById (request , id):
    try:
        rawMaterialsProduct = RawMaterialProduct.objects.get(id = id)        
        rawMaterialsProductSerializer = RawMaterialProductSerializer(rawMaterialsProduct)        
        return Response(rawMaterialsProductSerializer.data)
    except:
        return HttpResponse("Not Exist")

@api_view(['GET'])
def getByProductId(request, product_id):
    try:
        rawMaterialsProducts = RawMaterialProduct.objects.filter(product=product_id)
        rawMaterialsProductSerializer = RawMaterialProductSerializer(rawMaterialsProducts, many=True)
        return Response(rawMaterialsProductSerializer.data)
    except RawMaterialProduct.DoesNotExist:
        return Response([])
    
@api_view(['GET'])
def getname(request, name):
    try:
        rawMaterialsProducts = RawMaterialProduct.objects.get(name=name)
        rawMaterialsProductSerializer = RawMaterialProductSerializer(rawMaterialsProducts)
        return Response(rawMaterialsProductSerializer.data)
    except RawMaterialProduct.DoesNotExist:
        result = {
            'status': 'Category not found'
        }
        return Response(result, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update(request, product_id): 
    try:
        rawMaterialsProducts = RawMaterialProduct.objects.filter(product=product_id)        
        if not rawMaterialsProducts.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = request.data
        rawMaterialsProductUpdateSerializer = RawMaterialProductUpdateSerializer(data=data, many=True)

        if rawMaterialsProductUpdateSerializer.is_valid():
            for update_data in rawMaterialsProductUpdateSerializer.validated_data:
                rawMaterialProductId = update_data['id']
                rawMaterialsProduct = rawMaterialsProducts.get(id=rawMaterialProductId)
                rawMaterialsProduct.raw_material = update_data.get('raw_material', rawMaterialsProduct.raw_material)
                rawMaterialsProduct.rawmaterial_quantity = update_data.get('rawmaterial_quantity', rawMaterialsProduct.rawmaterial_quantity)
                rawMaterialsProduct.save()

            result = {'status': 'Done'}
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(rawMaterialsProductUpdateSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except RawMaterialProduct.DoesNotExist:
        return Response({'status': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)  
    
    
@api_view(['DELETE'])
def delete(request, product_id):
    try:
        raw_material_products = RawMaterialProduct.objects.filter(product=product_id)
    except ObjectDoesNotExist:
        return Response({'error': 'RawMaterialProduct not found'}, status=status.HTTP_404_NOT_FOUND)

    deleted_count, _ = raw_material_products.delete()

    if deleted_count > 0:
        result = {
            'status': 'deleted',
            'product_id': product_id
        }
        return Response(result, status=status.HTTP_200_OK)
    else:
        result = {
            'error': 'No RawMaterialProduct instances found for the given product_id'
        }
        return Response(result, status=status.HTTP_404_NOT_FOUND)





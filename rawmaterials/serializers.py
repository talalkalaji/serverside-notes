from rest_framework import serializers
from .models import RawMaterial

class RawMaterialSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    details = serializers.CharField()
    price = serializers.DecimalField(max_digits=12,decimal_places=2)
    quantity = serializers.DecimalField(max_digits=12,decimal_places=2)
    image = serializers.ImageField()
    
    def create(self, validated_data):
        return RawMaterial.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.details = validated_data.get('details', instance.details)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

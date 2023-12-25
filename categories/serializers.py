from rest_framework import serializers
from categories.models import Category

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    note = serializers.CharField()
    image = serializers.ImageField()
    
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.note = validated_data.get('note',instance.note)
        instance.image = validated_data.get('image',instance.image)
        instance.save()
        return instance

from products.models import Product
from rest_framework import serializers
from categories.models import Category

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    name = serializers.CharField()
    price = serializers.IntegerField()
    image = serializers.ImageField()
    details = serializers.CharField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category = validated_data.get('category',instance.category)
        instance.name = validated_data.get('name',instance.name)
        instance.price = validated_data.get('price',instance.price)
        instance.details = validated_data.get('details',instance.details)
        instance.image = validated_data.get('image',instance.image)

        instance.save(),
        return instance

from rest_framework import serializers
from .models import RawMaterialProduct
from rawmaterials.models import RawMaterial
from products.models import Product

class RawMaterialProductUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    raw_material = serializers.PrimaryKeyRelatedField(queryset=RawMaterial.objects.all())
    rawmaterial_quantity = serializers.IntegerField()

class RawMaterialProductListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        raw_material_product_mapping = {raw_material_product.id: raw_material_product for raw_material_product in instance}
        data_mapping = {item['id']: item for item in validated_data}
        ret = []
        for raw_material_product_id, data in data_mapping.items():
            raw_material_product = raw_material_product_mapping.get(raw_material_product_id, None)
            if raw_material_product is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(raw_material_product, data))

        for raw_material_product_id, raw_material_product in raw_material_product_mapping.items():
            if raw_material_product_id not in data_mapping:
                raw_material_product.delete()

        return ret

class RawMaterialProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    raw_material = serializers.PrimaryKeyRelatedField(queryset=RawMaterial.objects.all())
    rawmaterial_quantity = serializers.IntegerField()

    class Meta:
        list_serializer_class = RawMaterialProductListSerializer
        unique_together = ('product', 'raw_material',)

    def create(self, validated_data):
        return RawMaterialProduct.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.raw_material = validated_data.get('raw_material', instance.raw_material)
        instance.rawmaterial_quantity = validated_data.get('rawmaterial_quantity', instance.rawmaterial_quantity)
        instance.save()
        return instance

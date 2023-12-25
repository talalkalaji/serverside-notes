from rest_framework import serializers
from .models import RawMaterialSupplierBill
from rawmaterials.models import RawMaterial
from sup_bill.models import BillSupplier

class RawMaterialSupplierBillUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    supplier = serializers.PrimaryKeyRelatedField(queryset=BillSupplier.objects.all())
    rawMaterial = serializers.PrimaryKeyRelatedField(queryset=RawMaterial.objects.all())
    quantity = serializers.IntegerField()
    rawPrice = serializers.DecimalField(decimal_places=2, max_digits=12)

class RawMaterialSupplierBillListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        raw_material_supplier_bill_mapping = {bill.id: bill for bill in instance}
        data_mapping = {item['id']: item for item in validated_data}
        ret = []

        for bill_id, data in data_mapping.items():
            raw_material_supplier_bill = raw_material_supplier_bill_mapping.get(bill_id, None)
            if raw_material_supplier_bill is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(raw_material_supplier_bill, data))

        for bill_id, raw_material_supplier_bill in raw_material_supplier_bill_mapping.items():
            if bill_id not in data_mapping:
                raw_material_supplier_bill.delete()

        return ret

class RawMaterialSupplierBillSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    supplier = serializers.PrimaryKeyRelatedField(queryset=BillSupplier.objects.all())
    rawMaterial = serializers.PrimaryKeyRelatedField(queryset=RawMaterial.objects.all())
    date = serializers.DateField(read_only=True)
    edit_date = serializers.DateField(read_only=True)
    quantity = serializers.IntegerField()
    rawPrice = serializers.DecimalField(decimal_places=2, max_digits=12)
    quantityPrice = serializers.DecimalField(read_only=True   , max_digits=12, decimal_places=2)

    class Meta:
        list_serializer_class = RawMaterialSupplierBillListSerializer

    def create(self, validated_data):
        raw_material_supplier_bill = RawMaterialSupplierBill.objects.create(**validated_data)
        return raw_material_supplier_bill

    def update(self, instance, validated_data):
        instance.supplier = validated_data.get('supplier', instance.supplier)
        instance.rawMaterial = validated_data.get('rawMaterial', instance.rawMaterial)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.rawPrice = validated_data.get('rawPrice', instance.rawPrice)
        instance.quantityPrice = instance.quantity * instance.rawPrice
        raw_material = instance.rawMaterial
        raw_material.quantity += instance.quantity - instance._state.fields_cache['quantity']
        raw_material.save()
        instance.save()
        return instance


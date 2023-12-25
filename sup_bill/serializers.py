from rest_framework import serializers
from .models import BillSupplier
from supplier.serializers import SupplierSerializer
from supplier.models import Supplier

class BillSupplierUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only= True)
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    total = serializers.DecimalField(decimal_places=2, max_digits=12)
    paid = serializers.DecimalField(decimal_places=2, max_digits=12, required=False)
    date = serializers.DateField()
    details = serializers.CharField(max_length=30)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.supplier = validated_data.get('supplier', instance.supplier)
        instance.total = validated_data.get('total', instance.total)
        instance.paid = validated_data.get('paid', instance.paid)
        instance.date = validated_data.get('date', instance.date)
        instance.details = validated_data.get('details', instance.details)
        instance.due = instance.total - instance.paid
        instance.save()
        return instance
    
class BillSupplierListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        bill_supplier_mapping = {bill_supplier.id: bill_supplier for bill_supplier in instance}
        data_mapping = {item['id']: item for item in validated_data}
        ret = []
        for bill_supplier_id, data in data_mapping.items():
            bill_supplier = bill_supplier_mapping.get(bill_supplier_id, None)
            if bill_supplier is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(bill_supplier, data))

        # Perform deletions.
        for bill_supplier_id, bill_supplier in bill_supplier_mapping.items():
            if bill_supplier_id not in data_mapping:
                bill_supplier.delete()

        return ret

class BillSupplierSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    total = serializers.DecimalField(decimal_places=2, max_digits=12)
    paid = serializers.DecimalField(decimal_places=2, max_digits=12, required=False)
    due = serializers.DecimalField(decimal_places=2, max_digits=12, read_only=True)
    date = serializers.DateField()
    details = serializers.CharField(max_length=30)

    class Meta:
        list_serializer_class = BillSupplierListSerializer

    def create(self, validated_data):
        return BillSupplier.objects.create(**validated_data)
    
    
    
    
    



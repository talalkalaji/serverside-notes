from rest_framework import serializers
from table.serializers import TableSerializer
from .models import Bill

class BillSerializer(serializers.ModelSerializer):
    table = TableSerializer()

    class Meta:
        model = Bill
        fields = '__all__'

from rest_framework import serializers
from .models import *


class VendorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

        
class PurchaseOrderSerializer(serializers.ModelSerializer):
    Vendor = serializers.StringRelatedField(source='vendor.name', read_only = True)
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
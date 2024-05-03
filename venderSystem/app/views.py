from django.shortcuts import render
from django.http import HttpResponse
from .models import Vendor, PurchaseOrder
from .serializers import VendorsSerializer, PurchaseOrderSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import uuid
from django.core.exceptions import ObjectDoesNotExist

# Vendors API views
class CLVendors(APIView):

    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorsSerializer(vendors, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = VendorsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_uuid = uuid.uuid4()
            uuid_str = str(new_uuid)
            serializer.save(vendor_code=uuid_str)
            return Response({'status': 'created'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RUDVendors(APIView):

    def get(self, request, id):
        vendor = Vendor.objects.get(pk=id)
        serializer = VendorsSerializer(vendor, context={'request': request})
        return Response(serializer.data)

    def put(self, request, id):
        vendor = Vendor.objects.get(pk=id)
        serializer = VendorsSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        vendor = Vendor.objects.get(pk=id)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# PurchaseOrder API views
class CLPurchaseOrder(APIView):

    def get(self, request):
        orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(orders, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            product_order = serializer.save()

            # Assuming your vendor is associated with the product order
            vendor = product_order.vendor

            # Update performance metrics for the vendor
            vendor.update_metrics()
            vendor.save()
            return Response({'status': 'created'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RUDPurchaseOrder(APIView):

    def get(self, request, id):
        order = PurchaseOrder.objects.get(pk=id)
        serializer = PurchaseOrderSerializer(order, context={'request': request})
        return Response(serializer.data)

    def put(self, request, id):
        order = PurchaseOrder.objects.get(pk=id)
        serializer = PurchaseOrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        order = PurchaseOrder.objects.get(pk=id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Vendor performance API view
class VendorPerformance(APIView):
    def get_vendor_performance(self, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
            return vendor
        except Vendor.DoesNotExist:
            return None

    def get(self, request, vendor_id, format=None):
        vendor = self.get_vendor_performance(vendor_id)
        if vendor:
            performance_data = {
                'on_time_delivery_rate': vendor.on_time_delivery_rate,
                'quality_rating_avg': vendor.quality_rating_avg,
                'average_response_time': vendor.average_response_time,
                'fulfillment_rate': vendor.fulfillment_rate,
            }
            return Response(performance_data)
        return Response(status=status.HTTP_404_NOT_FOUND)


class AcknowledgePurchaseOrder(APIView):
    def post(self, request, po_id, format=None):
        try:
            purchase_order = PurchaseOrder.objects.get(pk=po_id)
        except PurchaseOrder.DoesNotExist:
            return Response({'error': 'Purchase Order not found'}, status=status.HTTP_404_NOT_FOUND)

        # Assuming you have a 'acknowledge' field in the PurchaseOrder model
        purchase_order.acknowledge = True
        purchase_order.save()

        # Trigger recalculation of average_response_time
        purchase_order.vendor.calculate_average_response_time()

        return Response({'status': 'acknowledged'})
    
'''
{
    "po_number": "PO004",
    "vendor": 4,
    "order_date": "2023-12-18T14:00:00Z",
    "delivery_date": "2023-12-25T14:00:00Z",
    "items": [{"name": "Accessory C", "quantity": 8, "price": 18.0}],
    "quantity": 8,
    "status": "pending",
    "quality_rating": null,
    "issue_date": "2023-12-18T13:00:00Z",
    "acknowledgment_date": "2023-12-18T15:30:00Z"
}

'''
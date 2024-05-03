from django.urls import path
from .views import *

urlpatterns = [
    path('api/vendors/', CLVendors.as_view(), name="CLVendors"),
    path('api/vendors/<int:id>/', RUDVendors.as_view(), name="RUDVendors"),
    path('api/purchase_orders/', CLPurchaseOrder.as_view(), name="CLPurchaseOrder"),
    path('api/purchase_orders/<int:id>/', RUDPurchaseOrder.as_view(), name="RUDPurchaseOrder"),
    path('api/vendors/<int:vendor_id>/performance/', VendorPerformance.as_view(), name='vendorPerformance'),
    path('api/purchase_orders/<int:po_id>/acknowledge/', AcknowledgePurchaseOrder.as_view(), name='acknowledge-purchase-order')
]

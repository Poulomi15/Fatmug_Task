# vendor_api/views.py
from audioop import avg
from rest_framework import generics
from vendor_management import vendor_api
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer

class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    acknowledged_orders = PurchaseOrder.objects.filter(vendor=vendor_api, acknowledgment_date__isnull=False)
    response_times = acknowledged_orders.aggregate(avg('acknowledgment_date' - 'issue_date'))['acknowledgment_date__avg'] or 0.0


class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = HistoricalPerformanceSerializer

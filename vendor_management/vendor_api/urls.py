# vendor_api/urls.py
from django.urls import path,include
from .views import VendorListCreateView, VendorDetailView, PurchaseOrderListCreateView, PurchaseOrderDetailView, VendorPerformanceView

urlpatterns = [
    path('api/vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('api/purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderDetailView.as_view(), name='purchase-order-detail'),
    path('api/vendors/<int:pk>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
    path('api/', include('vendor_api.urls')),  # Include vendor_api URLs
]

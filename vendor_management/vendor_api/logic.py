# vendor_api/logic.py
from django.db.models import Avg, Count
from django.utils import timezone
from .models import PurchaseOrder, Vendor

def calculate_on_time_delivery_rate(vendor):
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    on_time_delivery_orders = completed_orders.filter(delivery_date__lte=timezone.now())
    on_time_delivery_rate = (on_time_delivery_orders.count() / completed_orders.count()) * 100
    return on_time_delivery_rate

def calculate_quality_rating_avg(vendor):
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed').exclude(quality_rating__isnull=True)
    quality_rating_avg = completed_orders.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0.0
    return quality_rating_avg

def calculate_average_response_time(vendor):
    acknowledged_orders = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
    response_times = (acknowledged_orders.values('acknowledgment_date') - acknowledged_orders.values('issue_date')).aggregate(Avg('acknowledgment_date'))['acknowledgment_date__avg'] or 0.0
    return response_times.total_seconds() / 60  # Convert seconds to minutes

def calculate_fulfillment_rate(vendor):
    total_orders = PurchaseOrder.objects.filter(vendor=vendor)
    fulfilled_orders = total_orders.filter(status='completed').exclude(quality_rating__isnull=True)
    fulfillment_rate = (fulfilled_orders.count() / total_orders.count()) * 100
    return fulfillment_rate

def update_vendor_performance_metrics(vendor):
    # Update the vendor performance metrics
    vendor.on_time_delivery_rate = calculate_on_time_delivery_rate(vendor)
    vendor.quality_rating_avg = calculate_quality_rating_avg(vendor)
    vendor.average_response_time = calculate_average_response_time(vendor)
    vendor.fulfillment_rate = calculate_fulfillment_rate(vendor)
    vendor.save()

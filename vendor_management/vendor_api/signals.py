# vendor_api/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import PurchaseOrder

@receiver(post_save, sender=PurchaseOrder)
@receiver(post_delete, sender=PurchaseOrder)
def update_vendor_performance_on_order_change(sender, instance, **kwargs):
    from .logic import update_performance_metrics_on_order_completion, update_performance_metrics_on_acknowledgment
    if instance.status == 'completed':
        update_performance_metrics_on_order_completion(instance.id)
    elif instance.acknowledgment_date:
        update_performance_metrics_on_acknowledgment(instance.id)

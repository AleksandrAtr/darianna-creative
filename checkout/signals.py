from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Signal handler to update order total when a new OrderLineItem is saved or
    an existing one is updated.
    
    Args:
        sender: The model class that sent the signal.
        instance: The instance of the model that triggered the signal.
        created: A boolean indicating whether a new instance was created.
        **kwargs: Additional keyword arguments.
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Signal handler to update order total when an OrderLineItem is deleted.
    
    Args:
        sender: The model class that sent the signal.
        instance: The instance of the model that triggered the signal.
        **kwargs: Additional keyword arguments.
    """
    instance.order.update_total()

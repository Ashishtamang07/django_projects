from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Page
"""
configer signals:
write signals-> apps.py decelare ready()-> init.py default_app_config= 'account.apps.AccountConfig'
"""

@receiver(post_delete, sender= Page)
def delete_related_user(sender, instance, **kwargs):
    "page instance recived in instance "
    print("page post_delete", instance)
    instance.user.delete()

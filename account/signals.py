from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

from django.core.exceptions import ObjectDoesNotExist

# asagidaki deyirki User(sender) save olan anda asagidaki funqsiyaya(recever) xeber ele
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# bu asagidaki funqsiya save etmek isine baxir yuxarida yaradilani
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# ve elbetdeki ready adli funqsiyani Users-in terkibindeki apps.py-a elave edirik


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     try:
#         instance.profile.save()
#     except ObjectDoesNotExist:
#         Profile.objects.create(user=instance)
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from petstagram.accounts.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, create, **kwargs):
    if create:
        profile = Profile(
            user=instance,
        )

        profile.save()
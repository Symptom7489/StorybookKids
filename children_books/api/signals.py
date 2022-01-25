from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from children_books.models import Author

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name, email=instance.email)


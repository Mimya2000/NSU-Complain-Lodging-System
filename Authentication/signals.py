from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from .models import Faculty, Student, AdminEmployee


@receiver(post_save, sender=get_user_model())
def ProfileCreated(sender, instance, created, **kwargs):
    if created:
        user = instance
        if user.type == 'Faculty':
            profile = Faculty.objects.create(
                user=user,
            )
        elif user.type == 'Student':
            profile = Student.objects.create(
                user=user,
            )
        elif user.type == 'Administrator':
            profile = AdminEmployee.objects.create(
                user=user,
            )



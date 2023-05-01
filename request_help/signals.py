from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import HelpRequest
from categories.models import Donor
from django.conf import Settings

@receiver(post_save, sender=HelpRequest)
def send_help_request_notification(sender, instance, created, **kwargs):
    if created:
        subject = 'New Help Request'
        message = f'A new help request has been submitted:\n\nName: {instance.name}\nEmail: {instance.email}\nPhone: {instance.phone}\nMessage: {instance.message}'
        from_email = 'settings.EMAIL_HOST_USER'
        donor_emails = Donor.objects.values_list('email', flat=True)
        recipient_list = list(donor_emails)
        send_mail(subject, message, from_email, recipient_list)

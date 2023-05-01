from django.contrib import admin
from django.core.mail import send_mail
from .models import HelpRequest
from categories.models import Donor
from django.conf import Settings

class HelpRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'approved')
    actions = ['approve_requests', 'reject_requests']

    def approve_requests(self, request, queryset):
        queryset.update(approved=True)
        approved_requests = queryset.filter(approved=True)

        # Get the emails of all the donors
        donor_emails = Donor.objects.values_list('email', flat=True)

        # Send an email notification to the donors for approved requests
        subject = 'New Help Requests'
        message = 'New help requests have been submitted:\n\n'
        for help_request in approved_requests:
            message += f'Name: {help_request.name}\nEmail: {help_request.email}\nPhone: {help_request.phone}\nMessage: {help_request.message}\n\n'
        from_email = 'settings.EMAIL_HOST_USER'
        recipient_list = list(donor_emails)
        send_mail(subject, message, from_email, recipient_list)
    approve_requests.short_description = 'Approve selected help requests'

    def reject_requests(self, request, queryset):
        queryset.update(approved=False)
    reject_requests.short_description = 'Reject selected help requests'

admin.site.register(HelpRequest, HelpRequestAdmin)


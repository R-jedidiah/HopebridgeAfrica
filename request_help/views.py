from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import HelpRequestForm
from categories.models import Donor
from django.conf import Settings

def help_request(request):
    if request.method == 'POST':
        form = HelpRequestForm(request.POST)
        if form.is_valid():
            donor_emails = Donor.objects.values_list('email', flat=True)
            help_request = form.save()
            send_mail(
                'New help request',
                'A new help request has been submitted.',
                'settings.EMAIL_HOST_USER',
                ['donor_emails'],
                fail_silently=False,
            )
            messages.success(request, 'Your request has been submitted.')
            return redirect('home')
    else:
        form = HelpRequestForm()
    return render(request, 'request_help/requesthelp.html', {'form': form})

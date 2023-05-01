from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from categories.models import Donor
from .forms import DonorUpdateForm


def dashboard(request):
    donor = Donor.objects.get()
    context = {'donor': donor}
    return render(request, 'donor/dashboard.html', context)


@login_required
def update_donor(request, donor_id):
    donor = get_object_or_404(Donor, id=donor_id)

    if request.method == 'POST':
        form = DonorUpdateForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DonorUpdateForm(instance=donor)

    return render(request, 'donor/donor_update.html', {'form': form})

# @login_required
# def delete_donor(request, donor_id):
#     donor = get_object_or_404(Donor, id=donor_id)

#     if request.method == 'POST':
#         donor.delete()
#         return redirect('dashboard')

#     return render(request, 'dashboard.html', {'donor': donor})


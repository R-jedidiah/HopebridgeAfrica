from django.shortcuts import render, redirect
from django.template import RequestContext
from categories.models import Category
from categories.models import ChildrenHome
from django.shortcuts import render, get_object_or_404
from .forms import DonorForm
from .forms import ChildrenHomeForm
from django.contrib.auth.decorators import login_required
from categories.models import Donor
from django.db import IntegrityError
from django.core.mail import send_mail
from .forms import ContactForm
import os
from django.conf import settings




def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories.html', {'categories': categories})



def children_home_list(request):
    county = request.GET.get('county')
    children_homes = ChildrenHome.objects.all()
    if county:
        children_homes = children_homes.filter(county=county)
    context = {
        'children_homes': children_homes
    }
    return render(request, 'categories/children_home_list.html', context)

def childrenhome_detail(request, pk):
    childrenhome = get_object_or_404(ChildrenHome, pk=pk)
    context = {'childrenhome': childrenhome}
    return render(request, 'categories/childrenhome_detail.html', context)


@login_required
def donor_create(request):
    form = DonorForm()
    if request.method == "POST":
        form = DonorForm(request.POST)
        try:
            if form.is_valid():
                donor = form.save(commit=False)
                donor.user = request.user
                donor.save()
                return redirect('home')
        except IntegrityError:
                form.add_error('first_name', 'A donor with that username already exists.')    
    
    context = {
        'form':form
    }
    return render(request, 'categories/donor_create.html', context)


def ChildrenHome_create(request):
    form = ChildrenHomeForm()
    if request.method == "POST":
        form = ChildrenHomeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    
    context = {
        'form': form
    }
    return render(request, 'categories/childrenhome_create.html', context)

def contact_childrenhome(request, pk):
    childrenhome = ChildrenHome.objects.get(pk=pk)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # send email
            subject = f"Contact form submission from {name}"
            from_email = email
            to_email = childrenhome.email
            message = f"You have a new message from {name} ({email}):\n\n{message}"
            send_mail(subject, message, from_email, [to_email], fail_silently=False)

            # redirect to success page
            return render(request, 'success.html')
    else:
        form = ContactForm()

    context = {
        'form': form,
        'childrenhome': childrenhome,
    }
    return render(request, 'chilrenhome_detail.html', context)



def gallery(request, pk):
    # Retrieve the children's home object using the primary key from the URL.
    childrenhome = get_object_or_404(ChildrenHome, pk=pk)

    images = []
    # Use the primary key of the children's home to create the path to the subdirectory containing the images.
    images_dir = os.path.join(settings.MEDIA_ROOT, 'gallery', str(pk))
    for filename in os.listdir(images_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            path = os.path.join(images_dir, filename)
            title = os.path.splitext(filename)[0].title()
            images.append({'url': path, 'title': title})

    context = {'images': images, 'childrenhome': childrenhome}
    return render(request, 'categories/gallery.html', context)








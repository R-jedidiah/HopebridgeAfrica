from django.shortcuts import render, redirect
from categories.models import Category
from categories.models import ChildrenHome
from django.shortcuts import render, get_object_or_404
from .forms import DonorForm
from .forms import ChildrenHomeForm



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

def donor_create(request):
    form = DonorForm()
    if request.method == "POST":
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    
    context = {
        'form':form
    }
    return render(request, 'categories/donor_create.html', context)

def ChildrenHome_create(request):
    form = ChildrenHomeForm()
    if request.method == "POST":
        form = ChildrenHomeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    
    context = {
        'form': form
    }
    return render(request, 'categories/childrenhome_create.html', context)







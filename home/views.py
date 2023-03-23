from django.shortcuts import render

# Create your views here.

def base_home(request):
    return render(request, 'home/base_home.html')

def home(request):
    return render(request, 'home/home.html')
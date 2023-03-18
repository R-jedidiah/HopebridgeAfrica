from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import DonorSignUpForm
from .forms import SignInForm
from django.contrib import messages




# Create your views here.

def register(request):
    if request.method == 'POST':
        form = DonorSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            
            print('user created')

            
        
    else:
            form = DonorSignUpForm()
    return render(request, 'registration/signup.html', {'form':form})




def signin(request):
    if request.method == 'GET':
        # email = request.GET['email']
        # password = request.GET['password']
        user = authenticate(request, email='email', password='password')
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'registration/signin.html')






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
    
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'username or password is incorrect!')
        return render(request, 'registration/signin.html')
    
def logout_view(request):
    logout(request)
    return redirect('')





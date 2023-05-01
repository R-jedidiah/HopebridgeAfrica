from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import DonorSignUpForm
from .forms import SignInForm
from django.contrib import messages
from categories.models import Donor

def register(request):
    if request.method == 'POST':
        form = DonorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if User.objects.filter(username=user.username).exists():
                # If the username already exists, return an error message
                form.add_error('username', 'A user with that username already exists.')
            else:
                user.save()
                # Create a new donor object for the newly registered user
                donor = Donor.objects.create(user=user)
                # Log in the user
                login(request, user)
                return redirect('home')
    else:
        form = DonorSignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

            
        
    




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

def logout_on_session_expiry(request):
    if not request.session.get_expiry_age():
        logout(request)





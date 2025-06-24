from django.shortcuts import render, redirect
#from .models import Profile
from .forms import ProfileForm

# Create your views here.
def signin(request):
    return render(request, 'sign-in.html')

def signup(request):
    return render(request, 'sign-up.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def tables(request):
    return render(request, 'tables.html')

def profile(request):
    return render(request, 'profile.html')
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request,'main/dashboard.html')

def login_view(request):
    return render(request,'main/login.html')

def signup_view(request):
    return render(request,'main/signup.html')

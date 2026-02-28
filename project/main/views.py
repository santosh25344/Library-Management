from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.model import 

@login_required
def dashboard(request):
    return render(request,'main/dashboard.html')


def login_view(request):
    return render(request,'main/login.html')

def signup_view(request):
    if request.method=='POST':
        data=request.POST
        username=data['username']
        # user validation
        if len(data[username<6]):
            messages.error(request,'User Name must be 6 characters')
            context={
            'old_data': data,
                }
            return render(request,'main/signup.html')
        # password match validation
        if len(data[password])<6:
            messages.error(request,'password must be 5 characters')
            context={
                'old_data': data,
            
            }
            return render(request,'main/signup.html',context)
        else:
            if  data[password1]
            
            
        
            
        
    return render(request,'main/signup.html', context)

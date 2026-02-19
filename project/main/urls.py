from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('accounts/login/',views.login_view,name='login_view'),
    path('accounts/signup/',views.signup_view,name='signup_view'),
    
    
]
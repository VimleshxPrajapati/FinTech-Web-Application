from django.urls import path
from .views import kyc_registration,account,dashboard
app_name='account'
urlpatterns=[
    path('dashboard/',dashboard,name='dashboard'),
    path('',account,name='account'),
    path('kyc-reg/',kyc_registration,name='kyc-reg'),
]
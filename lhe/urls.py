from django.urls import path
from lhe.views import lhe_welcome

urlpatterns = [
    path('',lhe_welcome,name='lhe_welcome')    
]

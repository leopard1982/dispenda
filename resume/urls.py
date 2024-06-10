from django.urls import path
from resume.views import resume_welcome

urlpatterns = [
    path('',resume_welcome,name='resume_welcome')    
]

from django.shortcuts import render, HttpResponse

# Create your views here.
def resume_welcome(request):
    return HttpResponse('resume')
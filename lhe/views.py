from django.shortcuts import render, HttpResponse

def lhe_welcome(request):
    return HttpResponse("LHE men")
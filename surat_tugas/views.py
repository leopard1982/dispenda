from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view

# Create your views here.
def hello(request):
	return HttpResponse("hallo")
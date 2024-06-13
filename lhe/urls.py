from django.urls import path
from lhe.views import addLHE, addLHE_ok

urlpatterns = [
    path("add/",addLHE,name="addLHE"),
    path('add/1/',addLHE_ok,name="addLHE_ok")
]

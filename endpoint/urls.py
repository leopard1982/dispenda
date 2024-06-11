from django.urls import path
from endpoint.views import getPendingSurat

urlpatterns = [
    path('get/pendingsurat/', getPendingSurat, name="getPendingSurat"),
]

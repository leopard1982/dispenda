from django.urls import path
from surat_tugas.views import hello

urlpatterns = [
    path('', hello, name="hello"),

]

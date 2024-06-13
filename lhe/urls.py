from django.urls import path
from lhe.views import addLHE, addLHE_ok, addLHE_b1, delLHE_b1

urlpatterns = [
    path("add/",addLHE,name="addLHE"),
    path('add/1/',addLHE_ok,name="addLHE_ok"),
    path('add/b1/<str:id>/',addLHE_b1,name='addLHE_b1'),
    path('del/b1/<str:id>/<str:id_del>',delLHE_b1,name='delLHE_b1')
]

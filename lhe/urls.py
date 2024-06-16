from django.urls import path
from lhe.views import addLHE, addLHE_ok, addLHE_b1, delLHE_b1, addLHE_b2_a
from lhe.views import delLHE_b2_sasaran, delLHE_b2_tujuan, displayLHE, addLHE_b2_umum, delLHE_b2_umum

urlpatterns = [
    path("add/",addLHE,name="addLHE"),
    path('add/1/',addLHE_ok,name="addLHE_ok"),
    path('add/b1/<str:id>/',addLHE_b1,name='addLHE_b1'),
    path('del/b1/<str:id>/<str:id_del>',delLHE_b1,name='delLHE_b1'),
    path('add/b2/a/<str:id>/',addLHE_b2_a,name="addLHE_b2_a"),
    path('del/b2/a/s/<str:id>/<str:id_del>',delLHE_b2_sasaran, name="delLHE_b2_sasaran"),
    path('del/b2/a/t/<str:id>/<str:id_del>',delLHE_b2_tujuan, name="delLHE_b2_tujuan"),
    path('dis/',displayLHE,name="displayLHE"),
    path('add/b2/umum/<str:id>/',addLHE_b2_umum,name='addLHE_b2_umum'),
    path('del/b2/umum/<str:id>/<str:id_del>',delLHE_b2_umum,name='delLHE_b2_umum'),
]

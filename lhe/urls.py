from django.urls import path
from lhe.views import addLHE, addLHE_ok, addLHE_b1, delLHE_b1, addLHE_b2_a
from lhe.views import delLHE_b2_sasaran, delLHE_b2_tujuan, displayLHE, addLHE_b2_umum, delLHE_b2_umum
from lhe.views import addLHE_b2_ketatausahaan, delMobilPemkab, delMobilPemprov, delMotorPemprov
from lhe.views import delPegawaiDetail, delNorminatif, delKeuangan, delTanahBangunan
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
    path('add/b2/tu/<str:id>/',addLHE_b2_ketatausahaan,name="addLHE_b2_ketatausahaan"),
    path('del/b2/tu/<str:id>/<str:id_del>/',delPegawaiDetail,name="delPegawaiDetail"),
    path('del/b2/tu/norm/<str:id>/<str:id_del>/',delNorminatif,name="delNorminatif"),
    path('del/b2/tu/keu/<str:id>/<str:id_del>/',delKeuangan,name="delKeuangan"),
    path('del/b2/tu/ban/<str:id>/<str:id_del>/',delTanahBangunan,name="delTanahBangunan"),
    path('del/b2/tu/mobpk/<str:id>/<str:id_del>/',delMobilPemkab,name="delMobilPemkab"),
    path('del/b2/tu/mobpr/<str:id>/<str:id_del>/',delMobilPemprov,name="delMobilPemprov"),
    path('del/b2/tu/motor/<str:id>/<str:id_del>/',delMotorPemprov,name="delMotorPemprov")
]

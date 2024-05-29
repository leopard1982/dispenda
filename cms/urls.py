from django.urls import path
from cms.views import dashboard,  addGolongan, addJabatan, displayGolongan, displayJabatan
from cms.views import delGolongan, delJabatan, addPegawai, displayPegawai, delPegawai, addPengguna
from cms.views import displayPengguna, delPengguna, loginuser,logoutuser, displayLog 
from cms.views import displayGolonganID, displayJabatanID, displayPegawaiID, displayPenggunaID, displayLogID
from cms.views import addNomorSurat, displaySuratTugas, updateConfig
from cms.views import addDasarSurat, displayMasterDasarSurat,displayMasterDasarSuratID, delMasterDasarSuratTugas

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('auth/',loginuser,name='loginuser'),
    path('logout/',logoutuser,name='logoutuser'),
    path('master/gol/add/',addGolongan,name='addGolongan'),
    path('master/gol/dis/',displayGolongan,name='displayGolongan'),
    path('master/gol/dis/<str:id>',displayGolonganID,name='displayGolonganID'),
    path('master/gol/del/<str:id>/',delGolongan,name="delGolongan"),
    path('master/jab/add/',addJabatan,name='addJabatan'),
    path('master/jab/dis/',displayJabatan,name='displayJabatan'),
    path('master/jab/dis/<str:id>',displayJabatanID,name='displayJabatanID'),
    path('master/jab/del/<str:id>/',delJabatan,name="delJabatan"),
    path('master/peg/add/',addPegawai,name='addPegawai'),
    path('master/peg/dis/',displayPegawai,name='displayPegawai'),
    path('master/peg/dis/<str:id>',displayPegawaiID,name='displayPegawaiID'),
    path('master/peg/del/<str:id>/',delPegawai,name="delPegawai"),
    path('master/user/add/',addPengguna,name="addPengguna"),
    path('master/user/dis/',displayPengguna,name="displayPengguna"),
    path('master/user/dis/<str:id>',displayPenggunaID,name="displayPenggunaID"),
    path('master/user/del/<str:id>/',delPengguna,name="delPengguna"),
    path('logs/',displayLog,name="displayLog"),
    path('logs/<str:id>',displayLogID,name="displayLogID"),
    path('surat/add/',addNomorSurat,name='addNomorSurat'),
    path('surat/dis/',displaySuratTugas,name='displaySuratTugas'),
    path('master/sur/add/',addDasarSurat,name='addDasarSurat'),
    path('master/sur/dis/',displayMasterDasarSurat,name='displayMasterDasarSurat'),
    path('master/sur/dis/<str:id>',displayMasterDasarSuratID,name='displayMasterDasarSuratID'),
    path('master/sur/del/<str:id>/',delMasterDasarSuratTugas,name="delMasterDasarSuratTugas"),
    path('conf/',updateConfig,name="updateConfig"),
]

from django.urls import path
from cms.views import dashboard,  addGolongan, addJabatan, displayGolongan, displayJabatan
from cms.views import updateGolongan, updateJabatan, addPegawai, displayPegawai, updatePegawai, addPengguna
from cms.views import displayPengguna, delPengguna, loginuser,logoutuser, displayLog 
from cms.views import displayGolonganID, displayJabatanID, displayPegawaiID, displayPenggunaID, displayLogID
from cms.views import addNomorSurat, displaySuratTugas, updateConfig
from cms.views import addDasarSurat, displayMasterDasarSurat,displayMasterDasarSuratID, delMasterDasarSuratTugas
from cms.views import detailSuratTugas, detailSuratTugas_add_pegawai,detailSuratTugas_add_surat
from cms.views import detailSuratTugas_del_pegawai, detailSuratTugas_del_surat, detailSuratTugas_submit
from cms.views import delNomorSurat, Exportkan

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('auth/',loginuser,name='loginuser'),
    path('logout/',logoutuser,name='logoutuser'),
    path('master/gol/add/',addGolongan,name='addGolongan'),
    path('master/gol/dis/',displayGolongan,name='displayGolongan'),
    path('master/gol/dis/<str:id>',displayGolonganID,name='displayGolonganID'),
    path('master/gol/upd/',updateGolongan,name="updateGolongan"),
    path('master/jab/add/',addJabatan,name='addJabatan'),
    path('master/jab/dis/',displayJabatan,name='displayJabatan'),
    path('master/jab/dis/<str:id>',displayJabatanID,name='displayJabatanID'),
    path('master/jab/upd/',updateJabatan,name="updateJabatan"),
    path('master/peg/add/',addPegawai,name='addPegawai'),
    path('master/peg/dis/',displayPegawai,name='displayPegawai'),
    path('master/peg/dis/<str:id>',displayPegawaiID,name='displayPegawaiID'),
    path('master/peg/upd/',updatePegawai,name="updatePegawai"),
    path('master/user/add/',addPengguna,name="addPengguna"),
    path('master/user/dis/',displayPengguna,name="displayPengguna"),
    path('master/user/dis/<str:id>',displayPenggunaID,name="displayPenggunaID"),
    path('master/user/del/<str:id>/',delPengguna,name="delPengguna"),
    path('logs/',displayLog,name="displayLog"),
    path('logs/<str:id>',displayLogID,name="displayLogID"),
    path('surat/add/',addNomorSurat,name='addNomorSurat'),
    path('surat/del/<str:id>/',delNomorSurat,name='delNomorSurat'),
    path('surat/dis/',displaySuratTugas,name='displaySuratTugas'),
    path('master/sur/add/',addDasarSurat,name='addDasarSurat'),
    path('master/sur/dis/',displayMasterDasarSurat,name='displayMasterDasarSurat'),
    path('master/sur/dis/<str:id>/',displayMasterDasarSuratID,name='displayMasterDasarSuratID'),
    path('master/sur/del/<str:id>/',delMasterDasarSuratTugas,name="delMasterDasarSuratTugas"),
    path('conf/',updateConfig,name="updateConfig"),
    path('surat/add/<str:id>',detailSuratTugas,name='detailSuratTugas'),
    path('surat/add/dasar/',detailSuratTugas_add_surat,name='detailSuratTugas_add_surat'),
    path('surat/del/dasar/',detailSuratTugas_del_surat,name='detailSuratTugas_del_surat'),
    path('surat/add/peserta/',detailSuratTugas_add_pegawai,name='detailSuratTugas_add_pegawai'),
    path('surat/del/peserta/',detailSuratTugas_del_pegawai,name='detailSuratTugas_del_pegawai'),
    path('surat/submit/',detailSuratTugas_submit,name='detailSuratTugas_submit'),
    path('surat/export/<str:id>/',Exportkan,name="Exportkan")
]

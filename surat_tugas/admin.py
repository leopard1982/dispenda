from django.contrib import admin
from surat_tugas.models import TrxSuratTugas, MasterPegawai, MasterGolongan, MasterJabatan, Logging
from surat_tugas.models import ST_Peserta, ST_DasarTugas, MasterDasarST, ConfigDispenda, Pengguna


admin.site.register(TrxSuratTugas)
admin.site.register(MasterPegawai)
admin.site.register(ST_Peserta)
admin.site.register(ST_DasarTugas)
admin.site.register(MasterDasarST)
admin.site.register(ConfigDispenda)
admin.site.register(MasterGolongan)
admin.site.register(MasterJabatan)
admin.site.register(Pengguna)
admin.site.register(Logging)
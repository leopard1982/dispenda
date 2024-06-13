from django.contrib import admin
from lhe.models import simpulanHasilValBin,headerLHE,kepegawaianLHE,detailNormatifPegawai,simpulanPegawaiLHE

admin.site.register(headerLHE)
admin.site.register(simpulanHasilValBin)
admin.site.register(kepegawaianLHE)
admin.site.register(detailNormatifPegawai)
admin.site.register(simpulanPegawaiLHE)
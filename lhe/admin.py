from django.contrib import admin
from lhe.models import dataumumLHE,headerLHE,kepegawaianLHE,detailNormatifPegawai,simpulanPegawaiLHE

admin.site.register(headerLHE)
admin.site.register(dataumumLHE)
admin.site.register(kepegawaianLHE)
admin.site.register(detailNormatifPegawai)
admin.site.register(simpulanPegawaiLHE)
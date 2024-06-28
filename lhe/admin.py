from django.contrib import admin
from lhe.models import simpulanHasilValBin,headerLHE,bab2_tatausaha_kepegawaian_normatif,bab2_data_umum
from lhe.models import bab2_sasaran_evaluasi_pembinaan
from lhe.models import bab2_tatausaha_kepegawaian,bab2_tatausaha_kepegawaian_detail
from lhe.models import bab2_tujuan_evaluasi_pembinaan, bab2_tatausaha_keuangan
# from lhe.models import 

admin.site.register(headerLHE)
admin.site.register(simpulanHasilValBin)
admin.site.register(bab2_tatausaha_kepegawaian_normatif)
admin.site.register(bab2_data_umum)
admin.site.register(bab2_sasaran_evaluasi_pembinaan)
admin.site.register(bab2_tatausaha_kepegawaian)
admin.site.register(bab2_tatausaha_kepegawaian_detail)
admin.site.register(bab2_tujuan_evaluasi_pembinaan)
admin.site.register(bab2_tatausaha_keuangan)
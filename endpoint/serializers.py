from rest_framework import serializers 
from surat_tugas.models import TrxSuratTugas

class serialTrxSuratTugas(serializers.ModelSerializer):
	class Meta:
		model=TrxSuratTugas
		fields = "__all__"
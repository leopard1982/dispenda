from django.shortcuts import render
from surat_tugas.models import TrxSuratTugas
from endpoint.serializers import serialTrxSuratTugas
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getPendingSurat(request):
	if request.method=="GET":
		data=TrxSuratTugas.objects.all().filter(submit=False)
		serialnya = serialTrxSuratTugas(data,many=True)
		context={
			'statusCode':200,
			'data':serialnya.data
		}
		return Response(context)

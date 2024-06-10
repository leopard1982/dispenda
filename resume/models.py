from django.db import models
from surat_tugas.models import TrxSuratTugas
import uuid

class TrxResume(models.Model):
    id_resume = models.CharField(max_length=36,primary_key=True,default=str(uuid.uuid4()))
    suratTugas = models.ForeignKey(TrxSuratTugas,on_delete=models.RESTRICT)
    updatedBy = models.CharField(max_length=50)
    updatedAt = models.DateField(auto_now_add=False,blank=True,null=True)
    createdBy = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now_add=True,blank=True,null=True)
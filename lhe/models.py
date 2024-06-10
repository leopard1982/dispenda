from django.db import models
from surat_tugas.models import TrxSuratTugas
import uuid

class headerLHE(models.Model):
    id_lhe = models.CharField(max_length=36,primary_key=True,default=str(uuid.uuid4()))
    suratTugas = models.ForeignKey(TrxSuratTugas,on_delete=models.RESTRICT)
    nomor_lhe = models.CharField(max_length=50,blank=False,null=False,unique=True)
    tanggal_lhe = models.DateField(auto_now_add=False,null=True,blank=True)
    updatedBy = models.CharField(max_length=50)
    updatedAt = models.DateField(auto_now_add=False,blank=True,null=True)
    createdBy = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now_add=True,blank=True,null=True)


class dataumumLHE(models.Model):
    id_lhe = models.ForeignKey(headerLHE,on_delete=models.RESTRICT,blank=False,null=False)
    detail = models.CharField(max_length=200,blank=False,null=False)
    updatedBy = models.CharField(max_length=50)
    updatedAt = models.DateField(auto_now_add=False,blank=True,null=True)
    createdBy = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now_add=True,blank=True,null=True)

    class Meta:
        unique_together=['id_lhe','detail']

class kepegawaianLHE(models.Model):
    id_kepegawaian = models.CharField(max_length=36,primary_key=True,default=str(uuid.uuid4))
    id_lhe = models.ForeignKey(headerLHE,on_delete=models.RESTRICT)
    data_bulan = models.DateField(auto_now_add=False,blank=False,null=False)
    review = models.CharField(max_length=100,null=False,blank=False,default="b.	Pengelolaan administrasi kepegawaian sudah dilaksanakan dengan baik dan tertib.")
    updatedBy = models.CharField(max_length=50)
    updatedAt = models.DateField(auto_now_add=False,blank=True,null=True)
    createdBy = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now_add=True,blank=True,null=True)

class simpulanPegawaiLHE(models.Model):
    id_kepegawaian = models.ForeignKey(kepegawaianLHE,on_delete=models.RESTRICT)
    jenis = models.CharField(max_length=20,blank=False,null=False,verbose_name="Jenis Pegawai",default="")
    jumlah = models.SmallIntegerField(default=0,verbose_name="Jumlah Pegawai")
    updatedBy = models.CharField(max_length=50)
    updatedAt = models.DateField(auto_now_add=False,blank=True,null=True)
    createdBy = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now_add=True,blank=True,null=True)

class detailNormatifPegawai(models.Model):
    id_kepegawaian = models.ForeignKey(kepegawaianLHE,on_delete=models.RESTRICT)
    nama = models.CharField(max_length=100,blank=False,null=False,verbose_name="Nama Pegawai",default="")
    nip = models.CharField(max_length=50,blank=False,null=False,verbose_name="NIP Pegawai",default="")
    jabatan = models.CharField(max_length=50,blank=False,null=False,verbose_name="Nama Jabatan",default="")
    updatedBy = models.CharField(max_length=50)
    updatedAt = models.DateField(auto_now_add=False,blank=True,null=True)
    createdBy = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now_add=True,blank=True,null=True)
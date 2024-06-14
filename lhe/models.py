from django.db import models
from surat_tugas.models import TrxSuratTugas
import random
import uuid
import datetime

class headerLHE(models.Model):
    id_lhe = models.CharField(max_length=11,primary_key=True,default="")
    suratTugas = models.ForeignKey(TrxSuratTugas,on_delete=models.RESTRICT,verbose_name="Acuan Surat Tugas")
    nomor_lhe = models.CharField(max_length=50,blank=False,null=False,unique=True,verbose_name="Nomor Laporan Hasil Evaluasi")
    tanggal_lhe = models.DateField(auto_now_add=False,null=True,blank=True, verbose_name="Tanggal Laporan Hasil Evaluasi")
    updatedBy = models.CharField(max_length=50)
    updatedAt = models.DateField(auto_now_add=False,blank=True,null=True)
    createdBy = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now_add=True,blank=True,null=True)
    submit = models.BooleanField(default=False)

    class Meta:
        unique_together = ['nomor_lhe','suratTugas']

    def save(self,*args,**kwargs):
        self.id_lhe=uuid.uuid4()
        super(headerLHE,self).save(*args,**kwargs)
        TrxSuratTugas.objects.filter(nomor_surat=self.suratTugas).update(is_lhe=True)
        
class simpulanHasilValBin(models.Model):
    id_lhe = models.ForeignKey(headerLHE,on_delete=models.RESTRICT,blank=False,null=False)
    id_simpulan = models.CharField(max_length=36,primary_key=True,default=str(uuid.uuid4()))
    detail = models.CharField(max_length=200,blank=False,null=False)
    updatedBy = models.CharField(max_length=50)
    updatedAt = models.DateField(auto_now_add=False,blank=True,null=True)
    createdBy = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now_add=True,blank=True,null=True)

    def save(self,*args,**kwargs):
        self.id_simpulan=uuid.uuid4()
        super(simpulanHasilValBin,self).save(*args,**kwargs)

class bab2_tujuan_evaluasi_pembinaan(models.Model):
    id_lhe = models.ForeignKey(headerLHE,on_delete=models.RESTRICT,blank=False,null=False)
    id_tujuan = models.CharField(max_length=36,primary_key=True,default=str(uuid.uuid4()))
    detail = models.CharField(max_length=200,blank=False,null=False)
    createdBy = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now_add=True,blank=True,null=True)

    def save(self,*args,**kwargs):
        self.id_tujuan = uuid.uuid4()
        super(bab2_tujuan_evaluasi_pembinaan,self).save(*args,**kwargs)

class bab2_sasaran_evaluasi_pembinaan(models.Model):
    id_lhe = models.ForeignKey(headerLHE,on_delete=models.RESTRICT,blank=False,null=False)
    id_sasaran = models.CharField(max_length=36,primary_key=True,default=str(uuid.uuid4()))
    detail = models.CharField(max_length=200,blank=False,null=False)
    createdBy = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now_add=True,blank=True,null=True)

    def save(self,*args,**kwargs):
        self.id_sasaran = uuid.uuid4()
        super(bab2_sasaran_evaluasi_pembinaan,self).save(*args,**kwargs)

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
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


class MasterDasarST(models.Model):
    kode_dasar = models.CharField(max_length=10,unique=True,blank=False,primary_key=True) # type: ignore
    keterangan = models.CharField(max_length=50)
    updatedAt = models.DateTimeField(auto_now_add=True,null=True)
    updatedBy = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.keterangan

class MasterGolongan(models.Model):
    kode_golongan = models.CharField(max_length=10,primary_key=True,unique=True,blank=True,default="")
    keterangan = models.CharField(max_length=50)
    updatedAt = models.DateTimeField(auto_now_add=True,null=True)
    updatedBy = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.keterangan


class MasterJabatan(models.Model):
    kode_jabatan = models.CharField(max_length=10,primary_key=True,unique=True,blank=True,default="")
    keterangan = models.CharField(max_length=50)
    updatedAt = models.DateTimeField(auto_now_add=True,null=True)
    updatedBy = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.keterangan

class MasterPegawai(models.Model):
    nik = models.CharField(max_length=50,blank=False,primary_key=True,default="")
    nama = models.CharField(max_length=100,blank=False,null=False)
    kode_jabatan = models.ForeignKey(MasterJabatan,on_delete=models.RESTRICT)
    kode_golongan = models.ForeignKey(MasterGolongan,on_delete=models.RESTRICT)
    updatedAt = models.DateTimeField(auto_now_add=True,null=True)
    is_kepala = models.BooleanField(default=False)  
    updatedBy = models.CharField(max_length=20,blank=True,null=True)

    def save(self,*args,**kwargs):
        if self.is_kepala == True:
            if(MasterPegawai.objects.all().filter(is_kepala=True).count()>0):
                pass
            else:
                super(MasterPegawai,self).save(*args,**kwargs)
                ConfigDispenda.objects.create(
                    kepala = MasterPegawai.objects.get(nik=self.nik),
                    updatedBy = 'suryo'
                )
        else:
            if(ConfigDispenda.objects.all().count()>0):
                if(ConfigDispenda.objects.all()[0].kepala.nik==self.nik):
                    ConfigDispenda.objects.all().delete()
            super(MasterPegawai,self).save(*args,**kwargs)

    def __str__(self):
        jumlah=MasterPegawai.objects.all().filter(nik=self.nik).count()
        if jumlah>0:
            return self.nama
        else:
            return None
        
class ConfigDispenda(models.Model):
    is_PLT = models.BooleanField(default=False)
    kepala = models.ForeignKey(MasterPegawai,on_delete=models.RESTRICT)
    updatedBy = models.CharField(max_length=20,blank=True,null=True)
    updatedAt = models.DateTimeField(auto_now_add=True,null=True)

    def save(self,*args,**kwargs):
        if(self.kepala.is_kepala):
            if(ConfigDispenda.objects.all().count()>0):
                ConfigDispenda.objects.all().delete()
            super(ConfigDispenda,self).save(*args,**kwargs)
        else:
            return

    def __str__(self):
        return self.kepala.nama

class TrxSuratTugas(models.Model):
    nomor_surat = models.CharField(max_length=50,unique=True,blank=False,primary_key=True,default="")
    tgl_surat = models.DateField(auto_now_add=False,null=True)
    lokasi_surat = models.CharField(max_length=50)
    tujuan = models.CharField(max_length=50)
    lokasi = models.CharField(max_length=50)
    tgl_awal_tugas = models.DateField(auto_now_add=False,null=True)
    tgl_akhir_tugas = models.DateField(auto_now_add=False,null=True)
    updatedAt = models.DateTimeField(auto_now_add=True,null=True)
    kepala_nama = models.CharField(max_length=50,null=True,blank=True)
    kepala_nik = models.CharField(max_length=50,null=True,blank=True)
    kepala_jabatan = models.CharField(max_length=50,null=True,blank=True)
    kepala_golongan = models.CharField(max_length=50,null=True,blank=True)
    is_plt = models.BooleanField(default=False)
    submit = models.BooleanField(default=False)
    updatedBy = models.CharField(max_length=20,blank=True,null=True)

    def save(self,*args,**kwargs):
        if(ConfigDispenda.objects.all().count()>0):
            self.kepala_nama = ConfigDispenda.objects.all()[0].kepala.nama
            self.kepala_nik = ConfigDispenda.objects.all()[0].kepala.nik
            self.kepala_jabatan = ConfigDispenda.objects.all()[0].kepala.kode_jabatan.keterangan
            self.kepala_golongan = ConfigDispenda.objects.all()[0].kepala.kode_golongan.keterangan
            self.is_plt = ConfigDispenda.objects.all()[0].kepala.is_kepala
            super(TrxSuratTugas,self).save(*args,**kwargs)
        else:
            return

    def delete(self,*args,**kwargs):
        if self.submit:
            return
        else:
            super(TrxSuratTugas,self).delete(*args,**kwargs)

class ST_Peserta(models.Model):
    nomor_surat = models.ForeignKey(TrxSuratTugas,on_delete=models.RESTRICT)
    peserta = models.ForeignKey(MasterPegawai,on_delete=models.RESTRICT)
    updatedAt = models.DateTimeField(auto_now_add=True,null=True)
    updatedBy = models.CharField(max_length=20,blank=True,null=True)

    class Meta:
        unique_together=['nomor_surat','peserta']

    def save(self,*args,**kwargs):
        isSubmitted=TrxSuratTugas.objects.get(nomor_surat=self.nomor_surat.nomor_surat)
        if(not isSubmitted.submit):
            super(ST_Peserta,self).save(*args,**kwargs)
        else:
            return

    def delete(self,*args,**kwargs):
        isSubmitted=TrxSuratTugas.objects.get(nomor_surat=self.nomor_surat.nomor_surat)
        if(not isSubmitted.submit):
            super(ST_Peserta,self).delete(*args,**kwargs)
        else:
            return

class ST_DasarTugas(models.Model):
    nomor_surat = models.ForeignKey(TrxSuratTugas,on_delete=models.RESTRICT)
    dasar_tugas = models.ForeignKey(MasterDasarST,on_delete=models.RESTRICT)
    updatedAt = models.DateTimeField(auto_now_add=True,null=True)
    updatedBy = models.CharField(max_length=20,blank=True,null=True)

    class Meta:
        unique_together=['nomor_surat','dasar_tugas']

    def save(self,*args,**kwargs):
        # print(self.nomor_surat)
        isSubmitted=TrxSuratTugas.objects.get(nomor_surat=self.nomor_surat.nomor_surat)
        if not isSubmitted.submit :
            super(ST_DasarTugas,self).save(*args,**kwargs)
        else:
            return

    def delete(self,*args,**kwargs):
        isSubmitted=TrxSuratTugas.objects.get(nomor_surat=self.nomor_surat.nomor_surat)
        if(not isSubmitted.submit):
            super(ST_DasarTugas,self).delete(*args,**kwargs)
        else:
            return


class MasterPermission(models.Model):
    kode_permission = models.CharField(max_length=50,primary_key=True,default="")
    updatedAt = models.DateTimeField(auto_now_add=True,null=True)
    updatedBy = models.CharField(max_length=20,null=True,blank=True)

    
class MasterRole(models.Model):
    kode_role = models.CharField(max_length=50,primary_key=True,default="")
    permissions = models.JSONField()
    updatedAt = models.DateTimeField(auto_now_add=True,null=True)
    updatedBy = models.CharField(max_length=20,null=True,blank=True)

class Pengguna(AbstractUser):
    # role = models.ForeignKey(MasterRole,on_delete=models.RESTRICT)
    updatedAt = models.DateTimeField(auto_now_add=True,null=True)
    updatedBy = models.CharField(max_length=20,null=True,blank=True)
    is_edit = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    is_create = models.BooleanField(default=True)

class Logging(models.Model):
    updatedAt = models.DateTimeField(auto_now_add=True,null=True)
    user = models.ForeignKey(Pengguna,on_delete=models.RESTRICT)
    grouping = models.CharField(max_length=200,null=False,blank=True)
    transaction = models.CharField(max_length=250,null=False,blank=True,default="")

    def __str__(self):
        return f"{self.user} - {self.grouping} - {self.transaction}"
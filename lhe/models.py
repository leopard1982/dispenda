from django.db import models
from surat_tugas.models import TrxSuratTugas,MasterJabatan
import random
import uuid
import datetime
from django.db.models import Sum

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
    periode_awal = models.DateField(auto_now_add=False,blank=True,null=True)
    periode_akhir = models.DateField(auto_now_add=False,blank=True,null=True)

    class Meta:
        unique_together = ['nomor_lhe','suratTugas']

    def save(self,*args,**kwargs):
        self.id_lhe=uuid.uuid4()
        super(headerLHE,self).save(*args,**kwargs)
        TrxSuratTugas.objects.filter(nomor_surat=self.suratTugas).update(is_lhe=True)

    def __str__(self):
        return self.nomor_lhe
        
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
    
    class Meta:
        unique_together=['id_lhe','detail']

class bab2_tujuan_evaluasi_pembinaan(models.Model):
    id_lhe = models.ForeignKey(headerLHE,on_delete=models.RESTRICT,blank=False,null=False)
    id_tujuan = models.CharField(max_length=36,primary_key=True,default=str(uuid.uuid4()))
    detail = models.CharField(max_length=200,blank=False,null=False)
    createdBy = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now_add=True,blank=True,null=True)

    def save(self,*args,**kwargs):
        self.id_tujuan = uuid.uuid4()
        super(bab2_tujuan_evaluasi_pembinaan,self).save(*args,**kwargs)
    
    class Meta:
        unique_together=['id_lhe','detail']

class bab2_sasaran_evaluasi_pembinaan(models.Model):
    id_lhe = models.ForeignKey(headerLHE,on_delete=models.RESTRICT,blank=False,null=False)
    id_sasaran = models.CharField(max_length=36,primary_key=True,default=str(uuid.uuid4()))
    detail = models.CharField(max_length=200,blank=False,null=False)
    createdBy = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now_add=True,blank=True,null=True)

    def save(self,*args,**kwargs):
        self.id_sasaran = uuid.uuid4()
        super(bab2_sasaran_evaluasi_pembinaan,self).save(*args,**kwargs)

    class Meta:
        unique_together=['id_lhe','detail']

class bab2_data_umum(models.Model):
    id_lhe = models.ForeignKey(headerLHE,on_delete=models.RESTRICT,blank=False,null=False)
    id_data_umum = models.CharField(max_length=36,primary_key=True,default=str(uuid.uuid4()))
    detail = models.CharField(max_length=200,blank=False,null=False)
    createdBy = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now_add=True,blank=True,null=True)

    def save(self,*args,**kwargs):
        self.id_data_umum = uuid.uuid4()
        super(bab2_data_umum,self).save(*args,**kwargs)

    class Meta:
        unique_together=['id_lhe','detail']

class bab2_tatausaha_kepegawaian(models.Model):
    id_lhe = models.ForeignKey(headerLHE,on_delete=models.RESTRICT,blank=False,null=False)
    id_tu_kepegawaian = models.CharField(max_length=36,primary_key=True,default=str(uuid.uuid4()))
    periode = models.CharField(max_length=20,blank=False,null=False)
    UPPD = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=200)
    createdBy = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now_add=True,blank=True,null=True)

    def save(self,*args,**kwargs):
        lokasi_tugas = self.id_lhe.suratTugas.lokasi #mendapatkan lokasi surat tugas (link 3 table)
        self.UPPD = lokasi_tugas
        self.id_tu_kepegawaian= uuid.uuid4()
        super(bab2_tatausaha_kepegawaian,self).save(*args,**kwargs)

class bab2_tatausaha_kepegawaian_detail(models.Model):
    id_tu_kepegawaian = models.ForeignKey(bab2_tatausaha_kepegawaian,on_delete=models.RESTRICT)
    id_tu_kepegawaian_detail = models.CharField(max_length=36,primary_key=True,default=str(uuid.uuid4()))
    golongan = models.CharField(max_length=200,blank=False,null=False)
    jumlah = models.IntegerField(default=0)
    createdBy = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now_add=True,blank=True,null=True)

    def save(self,*args,**kwargs):
        self.id_tu_kepegawaian_detail = uuid.uuid4()
        super(bab2_tatausaha_kepegawaian_detail,self).save(*args,**kwargs)
    
    class Meta:
        unique_together=['id_tu_kepegawaian','golongan']

class bab2_tatausaha_kepegawaian_normatif(models.Model):
    id_tu_kepegawaian = models.ForeignKey(bab2_tatausaha_kepegawaian,on_delete=models.RESTRICT)
    id_tu_kepegawaian_normatif = models.CharField(max_length=36,primary_key=True,default=str(uuid.uuid4()))
    nama = models.CharField(max_length=200,blank=False,null=False)
    nip = models.CharField(max_length=200,blank=False,null=False)
    jabatan = models.ForeignKey(MasterJabatan,on_delete=models.RESTRICT)
    createdBy = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now_add=True,blank=True,null=True)

    def save(self,*args,**kwargs):
        self.id_tu_kepegawaian_normatif = uuid.uuid4()
        super(bab2_tatausaha_kepegawaian_normatif,self).save(*args,**kwargs)
    
    class Meta:
        unique_together=['id_tu_kepegawaian','nama','nip']

class bab2_tatausaha_keuangan(models.Model):
    id_lhe = models.ForeignKey(headerLHE,on_delete=models.RESTRICT)
    id_tu_keuangan = models.CharField(max_length=36,primary_key=True,default=str(uuid.uuid4()))
    detail = models.CharField(max_length=200,blank=False,null=False)
    createdBy = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now_add=True,blank=True,null=True)

    def save(self,*args,**kwargs):
        self.id_tu_keuangan = uuid.uuid4()
        super(bab2_tatausaha_keuangan,self).save(*args,**kwargs)
    
    class Meta:
        unique_together=['id_lhe','detail']

# #aset tidak bergerak
# class bab2_tatausaha_keuangan_a_tg(models.Model):
#     id_tu_keuangan = models.ForeignKey(headerLHE,on_delete=models.RESTRICT)
#     id_tu_a_tg = models.CharField(max_length=36,primary_key=True,default=str(uuid.uuid4()))
#     detail = models.CharField(max_length=200,blank=False,null=False)
#     createdBy = models.CharField(max_length=50)
#     createdAt = models.DateField(auto_now_add=True,blank=True,null=True)

#     def save(self,*args,**kwargs):
#         self.id_tu_a_tg = uuid.uuid4()
#         super(bab2_tatausaha_keuangan_a_tg,self).save(*args,**kwargs)
    
#     class Meta:
#         unique_together=['id_lhe','detail']


#aset tidak bergerak
class bab2_tatausaha_bangun_tanah(models.Model):
    id_lhe = models.ForeignKey(headerLHE,on_delete=models.RESTRICT)
    id_tu_bagun_tanah = models.CharField(max_length=36,primary_key=True,default=str(uuid.uuid4()))
    detail = models.CharField(max_length=200,blank=False,null=False)
    createdBy = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now_add=True,blank=True,null=True)

    def save(self,*args,**kwargs):
        self.id_tu_bagun_tanah= uuid.uuid4()
        super(bab2_tatausaha_bangun_tanah,self).save(*args,**kwargs)
    
    class Meta:
        unique_together=['id_lhe','detail']

class bab2_tatausaha_mobil_pemkab(models.Model):
    id_lhe = models.ForeignKey(headerLHE,on_delete=models.RESTRICT)
    id_tu_mobil_pemkab = models.CharField(max_length=36,primary_key=True,default=str(uuid.uuid4()))
    detail = models.CharField(max_length=200,blank=False,null=False)
    createdBy = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now_add=True,blank=True,null=True)

    def save(self,*args,**kwargs):
        self.id_tu_mobil_pemkab = uuid.uuid4()
        super(bab2_tatausaha_mobil_pemkab,self).save(*args,**kwargs)
    
    class Meta:
        unique_together=['id_lhe','detail']

class bab2_tatausaha_mobil_pemprov(models.Model):
    id_lhe = models.ForeignKey(headerLHE,on_delete=models.RESTRICT)
    id_tu_mobil_pemprov = models.CharField(max_length=36,primary_key=True,default=str(uuid.uuid4()))
    detail = models.CharField(max_length=200,blank=False,null=False)
    createdBy = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now_add=True,blank=True,null=True)

    def save(self,*args,**kwargs):
        self.id_tu_mobil_pemprov = uuid.uuid4()
        super(bab2_tatausaha_mobil_pemprov,self).save(*args,**kwargs)
    
    class Meta:
        unique_together=['id_lhe','detail']

class bab2_tatausaha_motor_pemprov(models.Model):
    id_lhe = models.ForeignKey(headerLHE,on_delete=models.RESTRICT)
    id_tu_motor_pemprov = models.CharField(max_length=36,primary_key=True,default=str(uuid.uuid4()))
    detail = models.CharField(max_length=200,blank=False,null=False)
    createdBy = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now_add=True,blank=True,null=True)

    def save(self,*args,**kwargs):
        self.id_tu_motor_pemprov = uuid.uuid4()
        super(bab2_tatausaha_motor_pemprov,self).save(*args,**kwargs)
    
    class Meta:
        unique_together=['id_lhe','detail']

BULAN = [
    (1,'JANUARI'),
    (2,'FEBRUARI'),
    (3,'MARET'),
    (4,'APRIL'),
    (5,'MEI'),
    (6,'JUNI'),
    (7,'JULI'),
    (8,'AGUSTUS'),
    (9,'SEPTEMBER'),
    (10,'OKTOBER'),
    (11,'NOVEMBER'),
    (12,'DESEMBER')
]
class bab3_pkb(models.Model):
    id_lhe = models.ForeignKey(headerLHE,on_delete=models.RESTRICT)
    id_pkb = models.CharField(max_length=36,primary_key=True,default=str(uuid.uuid4()))
    bulan_awal = models.PositiveSmallIntegerField(default=1,choices=BULAN)
    bulan_akhir = models.PositiveSmallIntegerField(default=12,choices=BULAN)
    tahun_awal = models.PositiveSmallIntegerField(default=2024)
    tahun_akhir = models.PositiveSmallIntegerField(default=2024)
    uppd = models.CharField(max_length=100,blank=True,null=True)
    keterangan = models.CharField(max_length=200)
    selisih_angka = models.BigIntegerField(default=0,blank=True,null=True)
    selisih_persen = models.FloatField(default=0.0,blank=True,null=True)
    createdBy = models.CharField(max_length=50,blank=False,null=False,default="")
    createdAt = models.CharField(max_length=50,blank=False,null=False,default="")
    is_periode = models.BooleanField(null=True,blank=True)
 
    def save(self,*args,**kwargs):
        self.uppd = self.id_lhe.suratTugas.lokasi
        self.selisih_angka=0
        self.selisih_persen=0
        if(self.bulan_awal<self.bulan_akhir and self.tahun_awal<self.tahun_akhir):
            super(bab3_pkb,self).save(*args,**kwargs)
            if(self.is_periode):
                bab3_pkb_detail.objects.all().filter(id_pkb=bab3_pkb.objects.get(id_pkb=self.id_pkb)).delete()
                for i in range(int(self.bulan_awal),int(self.bulan_akhir)+1):
                    detail = bab3_pkb_detail()
                    detail.id_pkb=bab3_pkb.objects.get(id_pkb=self.id_pkb)
                    detail.id_pkb_detail = str(uuid.uuid4())
                    detail.tahun_awal=self.tahun_awal
                    detail.tahun_akhir = self.tahun_akhir
                    detail.nilai_awal=0
                    detail.nilai_akhir=0
                    detail.bulan=i
                    detail.save()

class bab3_pkb_detail(models.Model):
    id_pkb = models.ForeignKey(bab3_pkb,on_delete=models.RESTRICT)
    id_pkb_detail = models.CharField(max_length=36,primary_key=True,default=str(uuid.uuid4()))
    bulan = models.PositiveSmallIntegerField(default=1,choices=BULAN)
    tahun_awal = models.PositiveSmallIntegerField(default=2024)
    tahun_akhir = models.PositiveSmallIntegerField(default=2024)
    nilai_awal = models.BigIntegerField(default=0)
    nilai_akhir = models.BigIntegerField(default=0)
    selisih_angka = models.BigIntegerField(default=0,blank=True,null=True)
    selisih_persen = models.FloatField(default=0.0,blank=True,null=True)
    createdBy = models.CharField(max_length=50,blank=False,null=False,default="")
    createdAt = models.CharField(max_length=50,blank=False,null=False,default="")

    def save(self,*args,**kwargs):
        self.selisih_angka=self.nilai_akhir-self.nilai_awal
        try:
            self.selisih_persen=(self.selisih_angka)/self.nilai_awal
        except:
            self.selisih_persen=0
        super(bab3_pkb_detail,self).save(*args,**kwargs)
        total_angka = bab3_pkb_detail.objects.all().filter(id_pkb=self.id_pkb).aggregate(Sum('selisih_angka'))
        total_persen = bab3_pkb_detail.objects.all().filter(id_pkb=self.id_pkb).aggregate(Sum('selisih_persen'))
        bab3_pkb.objects.all().filter(id_pkb=self.id_pkb.id_pkb).update(selisih_angka=total_angka['selisih_angka__sum'])
        bab3_pkb.objects.all().filter(id_pkb=self.id_pkb.id_pkb).update(selisih_persen=total_persen['selisih_persen__sum'])        

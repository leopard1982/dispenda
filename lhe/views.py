from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from lhe.models import headerLHE
from lhe.forms import inputHeaderLHE
from surat_tugas.models import TrxSuratTugas
import datetime

def getPendingSurat():
	return TrxSuratTugas.objects.all().filter(submit=False)

def getPendingLHE():
	return headerLHE.objects.all().filter(submit=False)

def addLHE(request):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	
	id_surattugas=""
	nomor_lhe=""
	tanggal_lhe=""
	
	if request.method == "POST":
		id_surattugas = request.POST['suratTugas']
		nomor_lhe = request.POST['nomor_lhe']
		tanggal_lhe = request.POST['tanggal_lhe']
		if tanggal_lhe=="":
			return HttpResponseRedirect('/lhe/add/')
		database = TrxSuratTugas.objects.get(id_surat=id_surattugas)
	
		context={
			'forms':inputHeaderLHE,
			'menuname':'Transaksi Evaluasi Tugas',
			'pathway':'Evaluasi Tugas - Menambah Evaluasi Tugas',
			'username':request.user.username,
			'id_surattugas':id_surattugas,
			'nomor_lhe':nomor_lhe,
			'tanggal_lhe':tanggal_lhe,
			'database':database,
			'pending_surat':getPendingSurat(),
			'pending_lhe':getPendingLHE()
			}
		
		request.session['status']=""
		return render(request,'lhe/create_lhe_detail.html',context)

	context={
		'forms':inputHeaderLHE,
		'menuname':'Transaksi Laporan Hasil Evaluasi',
		'pathway':'Laporan Hasil Evaluasi - Menambah Laporan Hasil Evaluasi',
		'username':request.user.username,
		'pending_surat':getPendingSurat(),
		'pending_lhe':getPendingLHE()
	}
	request.session['status']=""
	return render(request,'lhe/create_lhe.html',context)

def addLHE_ok(request):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
		
	if request.method == "POST":
		nomor_surat = request.POST['nomor_surat']
		nomor_lhe = request.POST['nomor_lhe']
		tanggal_lhe = request.POST['tanggal_lhe']
		print(tanggal_lhe)
		tahun = int(tanggal_lhe.split('-')[0])
		bulan = int(tanggal_lhe.split('-')[1])
		hari = int(tanggal_lhe.split('-')[2])
		tanggal_lhe=datetime.date(tahun,bulan,hari)
		headerlhe = headerLHE()
		headerlhe.suratTugas = TrxSuratTugas.objects.get(nomor_surat=nomor_surat)
		headerlhe.nomor_lhe = nomor_lhe
		headerlhe.tanggal_lhe = tanggal_lhe
		headerlhe.createdBy = request.user.username
		headerlhe.updatedBy = request.user.username
		headerlhe.updatedAt = datetime.datetime.now().date()
		try:
			headerlhe.save()
			return HttpResponseRedirect('/lhe/add/')
		except:
			return HttpResponse("error")

	# id_lhe = models.CharField(max_length=36,primary_key=True,default=str(uuid.uuid4()))
    # suratTugas = models.ForeignKey(TrxSuratTugas,on_delete=models.RESTRICT,verbose_name="Acuan Surat Tugas")
    # nomor_lhe = models.CharField(max_length=50,blank=False,null=False,unique=True,verbose_name="Nomor Laporan Hasil Evaluasi")
    # tanggal_lhe = models.DateField(auto_now_add=False,null=True,blank=True, verbose_name="Tanggal Laporan Hasil Evaluasi")
    # updatedBy = models.CharField(max_length=50)
    # updatedAt = models.DateField(auto_now_add=False,blank=True,null=True)
    # createdBy = models.CharField(max_length=50)
    # createdAt = models.DateField(auto_now_add=True,blank=True,null=True)
    # submit = models.BooleanField(default=False)		

	return HttpResponseRedirect('/lhe/add/')
	# context={
	# 	'forms':inputHeaderLHE,
	# 	'menuname':'Transaksi Laporan Hasil Evaluasi',
	# 	'pathway':'Laporan Hasil Evaluasi - Menambah Laporan Hasil Evaluasi',
	# 	'username':request.user.username,
	# }
	# request.session['status']=""
	# return render(request,'lhe/create_lhe.html',context)
	
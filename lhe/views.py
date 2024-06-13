from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from lhe.models import headerLHE, simpulanHasilValBin
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
		try:
			nomor_surat = request.POST['nomor_surat']
			nomor_lhe = request.POST['nomor_lhe']
			tanggal_lhe = request.POST['tanggal_lhe']
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
				return HttpResponseRedirect(f'/lhe/add/{headerlhe.id_lhe}/')
			except:
				return HttpResponseRedirect('/lhe/add/')
		except:
			pass
	return HttpResponseRedirect('/lhe/add/')

def addLHE_b1(request,id):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	
	headerlhe = headerLHE.objects.get(id_lhe=id)

	if request.method=="POST":
		detail_simpulan = request.POST['detail_simpulan']
		simpulan = simpulanHasilValBin()
		simpulan.updatedAt = datetime.datetime.now().date()
		simpulan.updatedBy = request.user.username
		simpulan.id_lhe = headerlhe
		simpulan.detail = detail_simpulan
		try:
			simpulan.save()
		except Exception as ex:
			print(ex)	
	simpulan_val_bin = simpulanHasilValBin.objects.filter(id_lhe=headerlhe)

	context = {
		'nomor_surat_tugas': headerlhe.suratTugas.nomor_surat,
		'tanggal_surat_tugas': headerlhe.suratTugas.tgl_surat,
		'lokasi_tugas':headerlhe.suratTugas.lokasi,
		'simpulan_val_bin':simpulan_val_bin,
		'id_lhe':headerlhe.id_lhe,
		'pending_surat':getPendingSurat(),
		'pending_lhe':getPendingLHE()
	}

	return render(request,'lhe/create_lhe_bab1.html',context)

def delLHE_b1(request,id,id_del):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	
	simpulanHasilValBin.objects.all().filter(id_simpulan=id_del).delete()

	return HttpResponseRedirect(f'/lhe/add/b1/{id}/')
	
	
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from lhe.models import headerLHE, simpulanHasilValBin
from lhe.forms import inputHeaderLHE, inputNormatifLHE, inputBab3PKB, inputBab3BNKB, inputBab3PAP
from surat_tugas.models import TrxSuratTugas, ST_Peserta, MasterJabatan
from lhe.models import bab2_sasaran_evaluasi_pembinaan, bab2_tujuan_evaluasi_pembinaan, bab2_data_umum
from lhe.models import bab2_tatausaha_kepegawaian, bab2_tatausaha_kepegawaian_detail, bab2_tatausaha_kepegawaian_normatif
from lhe.models import bab2_tatausaha_keuangan, bab3_pkb, bab3_pkb_detail, bab3_pap, bab3_pap_tahun1, bab3_pap_tahun2
import datetime
from django.core.paginator import Paginator
from lhe.models import bab2_tatausaha_bangun_tanah, bab2_tatausaha_mobil_pemkab, bab2_tatausaha_mobil_pemprov, bab2_tatausaha_motor_pemprov
from django.db.models import Sum
from lhe.models import bab3_bbnkb, bab3_bbnkb_detail

def getPendingSurat():
	return TrxSuratTugas.objects.all().filter(submit=False)

def getPendingLHE():
	return headerLHE.objects.all().filter(submit=False)

def angka1_9(angka):
		if(angka==1):
			return " satu "
		if(angka==2):
			return " dua "
		if(angka==3):
			return " tiga "
		if(angka==4):
			return " empat "
		if(angka==5):
			return " lima "
		if(angka==6):
			return " enam "
		if(angka==7):
			return " tujuh "
		if(angka==8):
			return " delapan "
		if(angka==9):
			return " sembilan "
		if(angka==0):
			return ""

def konversi_angka(angka:int):
	try:
		if(angka==0):
			return " belum ada "
		if(angka==1):
			return " satu "
		if(angka==2):
			return " dua "
		if(angka==3):
			return " tiga "
		if(angka==4):
			return " empat "
		if(angka==5):
			return " lima "
		if(angka==6):
			return " enam "
		if(angka==7):
			return " tujuh "
		if(angka==8):
			return " delapan "
		if(angka==9):
			return " sembilan "
		if(angka==10):
			return " sepuluh "
		if(angka==11):
			return " sebelas "
		if(angka==12):
			return " dua belas "
		if(angka==13):
			return " tiga belas "
		if(angka==14):
			return " empat belas "
		if(angka==15):
			return " lima belas "
		if(angka==16):
			return " enam belas "
		if(angka==17):
			return " tujuh belas "
		if(angka==18):
			return " delapan belas "
		if(angka==19):
			return " sembilan belas "
		if(angka==20):
			return " dua puluh "
		if angka>20:
			pul=int(angka/10)
			sat=angka%10
			return angka1_9(pul) + "puluh" + angka1_9(sat)
			
	except:
		return None
	
def konversi_bulan(bul:int):
	if(bul==1):
		return "JANUARI"
	if(bul==2):
		return "FEBRUARI"
	if(bul==3):
		return "MARET"
	if(bul==4):
		return "APRIL"
	if(bul==5):
		return "MEI"
	if(bul==6):
		return "JUNI"
	if(bul==7):
		return "JULI"
	if(bul==8):
		return "AGUSTUS"
	if(bul==9):
		return "SEPTEMBER"
	if(bul==10):
		return "OKTOBER"
	if(bul==11):
		return "NOVEMBER"
	if(bul==12):
		return "DESEMBER"
	

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

def displayLHE(request):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	try:
		page=request.GET['page']
	except:
		page=1
	if page==None:
		page=1

	listlhe = headerLHE.objects.all().order_by('-updatedAt')
	
	p=Paginator(listlhe,5)
	
	
	try:
		halaman = p.page(page)
	except:
		halaman = p.page(1)

	statusnya = request.session['status']
	request.session['status']=""
	
	context={
		'lists':halaman,
		'paginator':p,
		'menuname':'Daftar Laporan Hasil Evaluasi',
		'pathway':'Transaksi Hasil Evaluasi - Daftar Hasil Evaluasi',
		'username':request.user.username,
		'mywebsite': '/lhe/dis/',
		'status':statusnya,
		'pending_surat':getPendingSurat(),
		'pending_lhe':getPendingLHE()
	}

	return render(request,'lhe/display_lhe.html',context)


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
				return HttpResponseRedirect(f'/lhe/add/b1/{headerlhe.id_lhe}/')
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
			print('yehehehe')   
   	
	simpulan_val_bin = simpulanHasilValBin.objects.filter(id_lhe=headerlhe)
 
	statusnya = request.session['status']
	request.session['status']=""     

	context = {
		'nomor_lhe':headerlhe.nomor_lhe,
		'nomor_surat_tugas': headerlhe.suratTugas.nomor_surat,
		'tanggal_surat_tugas': headerlhe.suratTugas.tgl_surat,
		'lokasi_tugas':headerlhe.suratTugas.lokasi,
		'simpulan_val_bin':simpulan_val_bin,
		'id_lhe':headerlhe.id_lhe,
		'pending_surat':getPendingSurat(),
		'pending_lhe':getPendingLHE(),
		'status':statusnya
	}

	return render(request,'lhe/create_lhe_bab1.html',context)

def delLHE_b1(request,id,id_del):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	
	simpulanHasilValBin.objects.all().filter(id_simpulan=id_del).delete()

	return HttpResponseRedirect(f'/lhe/add/b1/{id}/')

#bab2 bagian a --> 
def addLHE_b2_a(request,id):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	#mendapatkan headerLHE
	headerlhe = headerLHE.objects.get(id_lhe=id)

	if request.method=="POST":
		if('tujuan' in request.POST):
			# request.POST['tujuan']
			#menambah tujuan
			tujuan=bab2_tujuan_evaluasi_pembinaan()
			tujuan.createdAt=datetime.datetime.now().date()
			tujuan.createdBy=request.user.username
			tujuan.detail=request.POST['tujuan']
			tujuan.id_lhe=headerlhe
			try:
				tujuan.save()
			except:
				pass
		if('sasaran' in request.POST):
			# sasaran=request.POST['sasaran']
			sasaran=bab2_sasaran_evaluasi_pembinaan()
			sasaran.createdAt=datetime.datetime.now().date()
			sasaran.createdBy=request.user.username
			sasaran.detail=request.POST['sasaran']
			sasaran.id_lhe=headerlhe
			try:
				sasaran.save()
			except:
				pass
		if('awal_periode' in request.POST):
			awal=request.POST['awal_periode']
			akhir=request.POST['akhir_periode']
			headerLHE.objects.all().filter(id_lhe=id).update(periode_awal=datetime.date(year=int(awal.split('-')[0]),month=int(awal.split('-')[1]),day=int(awal.split('-')[2])))
			headerLHE.objects.all().filter(id_lhe=id).update(periode_akhir=datetime.date(year=int(akhir.split('-')[0]),month=int(akhir.split('-')[1]),day=int(akhir.split('-')[2])))
			headerlhe = headerLHE.objects.get(id_lhe=id)
			return HttpResponseRedirect(f'/lhe/add/b2/umum/{id}')

	tujuan_evaluasi = bab2_tujuan_evaluasi_pembinaan.objects.all().filter(id_lhe=headerlhe)
	sasaran_evaluasi = bab2_sasaran_evaluasi_pembinaan.objects.all().filter(id_lhe=headerlhe)
	#filtering surat tugas
	trxsurattugas = TrxSuratTugas.objects.get(nomor_surat=headerlhe.suratTugas)
	peserta = ST_Peserta.objects.all().filter(id_surat=trxsurattugas)
	
	try:
		periode_awal=f"{str(headerlhe.periode_awal).split('-')[0]}-{str(headerlhe.periode_awal).split('-')[1]}-{str(headerlhe.periode_awal).split('-')[2]}"
	except:
		periode_awal=None
	try:
		periode_akhir=f"{str(headerlhe.periode_akhir).split('-')[0]}-{str(headerlhe.periode_akhir).split('-')[1]}-{str(headerlhe.periode_akhir).split('-')[2]}"
	except:
		periode_akhir=None

	statusnya = request.session['status']
	request.session['status']=""

	context = {
		'nomor_lhe':headerlhe.nomor_lhe,
		'nomor_surat_tugas': headerlhe.suratTugas.nomor_surat,
		'tanggal_surat_tugas': headerlhe.suratTugas.tgl_surat,
		'lokasi_tugas':headerlhe.suratTugas.lokasi,
		'id_lhe':headerlhe.id_lhe,
		'tujuan_evaluasi':tujuan_evaluasi,
		'sasaran_evaluasi':sasaran_evaluasi,
		'pending_surat':getPendingSurat(),
		'pending_lhe':getPendingLHE(),
		'trxsurattugas':trxsurattugas,
		'peserta':peserta,
		'periode_awal':periode_awal,
		'periode_akhir':periode_akhir,
		'status':statusnya
	}
	return render(request,'lhe/create_lhe_bab2_a.html',context)
	
def delLHE_b2_tujuan(request,id,id_del):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	print(id)
	print(id_del)
	bab2_tujuan_evaluasi_pembinaan.objects.all().filter(id_tujuan=id_del).delete()

	return HttpResponseRedirect(f'/lhe/add/b2/a/{id}/')

def delLHE_b2_sasaran(request,id,id_del):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	
	bab2_sasaran_evaluasi_pembinaan.objects.all().filter(id_sasaran=id_del).delete()

	return HttpResponseRedirect(f'/lhe/add/b2/a/{id}/')

def addLHE_b2_umum(request,id):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	#mendapatkan headerLHE
	headerlhe = headerLHE.objects.get(id_lhe=id)

	if request.method=="POST":
		if('data_umum' in request.POST):
			# request.POST['tujuan']
			#menambah tujuan
			tujuan=bab2_data_umum()
			tujuan.createdAt=datetime.datetime.now().date()
			tujuan.createdBy=request.user.username
			tujuan.detail=request.POST['data_umum']
			tujuan.id_lhe=headerlhe
			try:
				tujuan.save()
			except:
				pass
	data_umum = bab2_data_umum.objects.all().filter(id_lhe=headerlhe)

	statusnya = request.session['status']
	request.session['status']=""

	context = {
		'nomor_lhe':headerlhe.nomor_lhe,
		'id_lhe':headerlhe.id_lhe,
		'pending_surat':getPendingSurat(),
		'pending_lhe':getPendingLHE(),		
		'data_umum':data_umum,
		'status':statusnya
	}
	return render(request,'lhe/create_lhe_bab2_a_dataumum.html',context)

def delLHE_b2_umum(request,id,id_del):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	
	bab2_data_umum.objects.all().filter(id_data_umum=id_del).delete()

	return HttpResponseRedirect(f'/lhe/add/b2/umum/{id}/')

def addLHE_b2_ketatausahaan(request,id):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')

	headerlhe = headerLHE.objects.get(id_lhe=id)
	fKeuangan = False
	fKepegawaian = False
	fBMD = False

	if request.method=="POST":
		if 'periode' in request.POST:
			pegawai=bab2_tatausaha_kepegawaian.objects.filter(id_lhe=id)
			if(pegawai.count()>0):
				pegawai.update(
					periode=request.POST['periode'],
					createdAt=datetime.datetime.now().date(),
					createdBy=request.user.username
				)
			else:
				bab2_tatausaha_kepegawaian.objects.create(
					id_lhe=headerlhe,
					periode=request.POST['periode'],
					createdAt=datetime.datetime.now().date(),
					createdBy=request.user.username
				) 
			fKepegawaian=True
		if 'golongan' in request.POST:
			try:
				id_tu_kepegawaian = bab2_tatausaha_kepegawaian.objects.get(id_lhe=id).id_tu_kepegawaian
				detail = bab2_tatausaha_kepegawaian_detail()
				detail.id_tu_kepegawaian = bab2_tatausaha_kepegawaian.objects.get(id_tu_kepegawaian=id_tu_kepegawaian)
				detail.golongan = request.POST['golongan']
				detail.jumlah=int(request.POST['jumlah'])
				detail.createdAt=datetime.datetime.now().date()
				detail.createdBy=request.user.username
				detail.save()
			except:
				pass
			fKepegawaian=True
			
		if 'nip' in request.POST:
			try:
				id_tu_kepegawaian = bab2_tatausaha_kepegawaian.objects.get(id_lhe=id).id_tu_kepegawaian
				normatif = bab2_tatausaha_kepegawaian_normatif()
				normatif.id_tu_kepegawaian = bab2_tatausaha_kepegawaian.objects.get(id_tu_kepegawaian=id_tu_kepegawaian)
				normatif.jabatan = MasterJabatan.objects.get(kode_jabatan=request.POST['jabatan'])
				normatif.nip = request.POST['nip']
				normatif.nama = request.POST['nama']
				normatif.createdAt=datetime.datetime.now().date()
				normatif.createdBy=request.user.username
				normatif.save()
			except Exception as ex:
				print(ex)
			fKepegawaian=True

		if 'keuangan' in request.POST:
			try:
				keuangan = bab2_tatausaha_keuangan()
				keuangan.id_lhe=headerlhe
				keuangan.detail=request.POST['keuangan']
				keuangan.createdAt=datetime.datetime.now().date()
				keuangan.createdBy=request.user.username
				keuangan.save()
			except Exception as ex:
				print(ex)
			fKeuangan=True
		
		if 'aset_tak_bergerak' in request.POST:
			try:
				aset = bab2_tatausaha_bangun_tanah()
				aset.createdBy = request.user.username
				aset.createdAt = datetime.datetime.now().date()
				aset.detail=request.POST['aset_tak_bergerak']
				aset.id_lhe = headerlhe
				aset.save()
			except Exception as ex:
				print(ex)
				pass
			fBMD=True

		if 'mobil_pemkab' in request.POST:
			try:
				aset = bab2_tatausaha_mobil_pemkab()
				aset.createdBy = request.user.username
				aset.createdAt = datetime.datetime.now().date()
				aset.detail=request.POST['mobil_pemkab']
				aset.id_lhe = headerlhe
				aset.save()
			except Exception as ex:
				print(ex)
				pass
			fBMD=True

		if 'mobil_pemprov' in request.POST:
			try:
				aset = bab2_tatausaha_mobil_pemprov()
				aset.createdBy = request.user.username
				aset.createdAt = datetime.datetime.now().date()
				aset.detail=request.POST['mobil_pemprov']
				aset.id_lhe = headerlhe
				aset.save()
			except Exception as ex:
				print(ex)
				pass
			fBMD=True

		if 'motor_pemprov' in request.POST:
			try:
				aset = bab2_tatausaha_motor_pemprov()
				aset.createdBy = request.user.username
				aset.createdAt = datetime.datetime.now().date()
				aset.detail=request.POST['motor_pemprov']
				aset.id_lhe = headerlhe
				aset.save()
			except Exception as ex:
				print(ex)
				pass
			fBMD=True

	try:
		tu_header = bab2_tatausaha_kepegawaian.objects.get(id_lhe=headerlhe)
	except:
		tu_header = None
	
	lokasi = headerlhe.suratTugas.lokasi
	tu_detail = bab2_tatausaha_kepegawaian_detail.objects.all().filter(id_tu_kepegawaian=tu_header)
	tu_normatif = bab2_tatausaha_kepegawaian_normatif.objects.all().filter(id_tu_kepegawaian=tu_header)
	tu_keuangan = bab2_tatausaha_keuangan.objects.all().filter(id_lhe=headerlhe)
	aset_tak_bergerak = bab2_tatausaha_bangun_tanah.objects.all().filter(id_lhe=headerlhe)
	mobil_pemkab = bab2_tatausaha_mobil_pemkab.objects.all().filter(id_lhe=headerlhe)
	jml_mobil_pemkab = konversi_angka(mobil_pemkab.count())
	mobil_pemprov = bab2_tatausaha_mobil_pemprov.objects.all().filter(id_lhe=headerlhe)
	jml_mobil_pemprov = konversi_angka(mobil_pemprov.count())
	motor_pemprov = bab2_tatausaha_motor_pemprov.objects.all().filter(id_lhe=headerlhe)
	jml_motor_pemprov = konversi_angka(motor_pemprov.count())
	forms = inputNormatifLHE()
	statusnya = request.session['status']
	request.session['status']=""

	context = {
		'nomor_lhe':headerlhe.nomor_lhe,
		'id_lhe':headerlhe.id_lhe,
		'pending_surat':getPendingSurat(),
		'pending_lhe':getPendingLHE(),		
		'tu_header':tu_header,
		'tu_detail':tu_detail,
		'tu_normatif':tu_normatif,
		'forms':forms,
		'lokasi':lokasi,
		'tu_keuangan':tu_keuangan,
		'fKepegawaian':fKepegawaian,
		'fKeuangan':fKeuangan,
		'fBMD':fBMD,
		'aset_tak_bergerak':aset_tak_bergerak,
		'mobil_pemkab':mobil_pemkab,
		'jml_mobil_pemkab':jml_mobil_pemkab,
		'mobil_pemprov':mobil_pemprov,
		'jml_mobil_pemprov':jml_mobil_pemprov,
		'motor_pemprov':motor_pemprov,
		'jml_motor_pemprov':jml_motor_pemprov,
		'status':statusnya
	}
	return render(request,'lhe/create_lhe_bab2_c_ketatausahaan.html',context)

def delPegawaiDetail(request,id,id_del):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	
	bab2_tatausaha_kepegawaian_detail.objects.all().filter(id_tu_kepegawaian_detail=id_del).delete()

	return HttpResponseRedirect(f'/lhe/add/b2/tu/{id}/')

def delNorminatif(request,id,id_del):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	
	bab2_tatausaha_kepegawaian_normatif.objects.all().filter(id_tu_kepegawaian_normatif=id_del).delete()

	return HttpResponseRedirect(f'/lhe/add/b2/tu/{id}/')

def delKeuangan(request,id,id_del):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	
	bab2_tatausaha_keuangan.objects.all().filter(id_tu_keuangan =id_del).delete()

	return HttpResponseRedirect(f'/lhe/add/b2/tu/{id}/')

def delTanahBangunan(request,id,id_del):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	
	bab2_tatausaha_bangun_tanah.objects.all().filter(id_tu_bagun_tanah=id_del).delete()

	return HttpResponseRedirect(f'/lhe/add/b2/tu/{id}/')

def delMobilPemkab(request,id,id_del):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	
	bab2_tatausaha_mobil_pemkab.objects.all().filter(id_tu_mobil_pemkab=id_del).delete()

	return HttpResponseRedirect(f'/lhe/add/b2/tu/{id}/')

def delMobilPemprov(request,id,id_del):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	
	bab2_tatausaha_mobil_pemprov.objects.all().filter(id_tu_mobil_pemprov=id_del).delete()

	return HttpResponseRedirect(f'/lhe/add/b2/tu/{id}/')

def delMotorPemprov(request,id,id_del):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	
	bab2_tatausaha_motor_pemprov.objects.all().filter(id_tu_motor_pemprov=id_del).delete()

	return HttpResponseRedirect(f'/lhe/add/b2/tu/{id}/')

def addLHE_b2_pkb(request,id):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')

	headerlhe = headerLHE.objects.get(id_lhe=id)
	
	acc_pkb=False
	acc_piutang=False
	acc_penetapan=False

	obj_data_piutang = 0
	obj_data_piutang_nominal = 0
	obj_pelunasan_piutang = 0
	obj_pelunasan_piutang_persen =0
	pelunasan_piutang_rupiah=0
	pelunasan_piutang_persen=0
	jml_pkb_roda4_angka = 0
	jml_pkb_kuning_angka = 0
	jml_pkb_hitam_angka = 0
	jml_pkb_roda4_huruf = ""
	jml_pkb_kuning_huruf = ""
	jml_pkb_hitam_huruf = ""
	penelitian_ulang=0

	if request.method == "POST":
		#apakah update piutang?
		#cek dolo
		try:
			if 'jml_pkb_roda4' in request.POST:
				if(int(request.POST['jml_pkb_roda4'])<100):
					pkb = bab3_pkb.objects.get(id_lhe=headerlhe)
					pkb.jml_pkb_roda4=request.POST['jml_pkb_roda4']
					pkb.is_periode=False
					pkb.is_new=False
					pkb.save()
					acc_penetapan=True
					request.session['status']="Data Jumlah PKB Roda 4 berhasil diupdate"

			if 'jml_pkb_kuning' in request.POST:
				if(int(request.POST['jml_pkb_kuning'])<100):
					pkb = bab3_pkb.objects.get(id_lhe=headerlhe)
					pkb.jml_pkb_kuning=request.POST['jml_pkb_kuning']
					pkb.is_periode=False
					pkb.is_new=False
					pkb.save()
					acc_penetapan=True
					request.session['status']="Data Jumlah PKB Plat Kuning berhasil diupdate"

			if 'jml_pkb_hitam' in request.POST:
				if(int(request.POST['jml_pkb_hitam'])<100):
					pkb = bab3_pkb.objects.get(id_lhe=headerlhe)
					pkb.jml_pkb_hitam=request.POST['jml_pkb_hitam']
					pkb.is_periode=False
					pkb.is_new=False
					pkb.save()
					acc_penetapan=True
					request.session['status']="Data Jumlah PKB Plat Hitam berhasil diupdate"

			if 'penelitian_ulang' in request.POST:
				if(int(request.POST['penelitian_ulang'])<100):
					pkb = bab3_pkb.objects.get(id_lhe=headerlhe)
					pkb.penelitian_ulang=request.POST['penelitian_ulang']
					pkb.is_periode=False
					pkb.is_new=False
					pkb.save()
					acc_penetapan=True
					request.session['status']="Data Jumlah PKB penelitian ulang berhasil diupdate"

			if 'obj_data_piutang' in request.POST:
				pkb = bab3_pkb.objects.get(id_lhe=headerlhe)
				pkb.obj_data_piutang=request.POST['obj_data_piutang']
				pkb.is_periode=False
				pkb.is_new=False
				pkb.save()
				acc_piutang=True
				request.session['status']="Data Jumlah Piutang PKB berhasil diupdate"
			
			if 'obj_data_piutang_nominal' in request.POST:
				pkb = bab3_pkb.objects.get(id_lhe=headerlhe)
				pkb.obj_data_piutang_nominal=request.POST['obj_data_piutang_nominal']
				pkb.is_periode=False
				pkb.is_new=False
				pkb.save()
				acc_piutang=True
				request.session['status']="Data Rupiah PKB berhasil diupdate"
			
			if 'obj_pelunasan_piutang' in request.POST:
				pkb = bab3_pkb.objects.get(id_lhe=headerlhe)
				pkb.obj_pelunasan_piutang=request.POST['obj_pelunasan_piutang']
				pkb.is_periode=False
				pkb.is_new=False
				pkb.save()
				acc_piutang=True
				request.session['status']="Data Pelunasan Piutan PKB berhasil diupdate"

			if 'obj_pelunasan_piutang_persen' in request.POST:
				pkb = bab3_pkb.objects.get(id_lhe=headerlhe)
				pkb.obj_pelunasan_piutang_persen=request.POST['obj_pelunasan_piutang_persen']
				pkb.is_periode=False
				pkb.is_new=False
				pkb.save()
				acc_piutang=True
				request.session['status']="Data Persentase Pelunasan PKB berhasil diupdate"

			if 'pelunasan_piutang_rupiah' in request.POST:
				pkb = bab3_pkb.objects.get(id_lhe=headerlhe)
				pkb.pelunasan_piutang_rupiah=request.POST['pelunasan_piutang_rupiah']
				pkb.is_periode=False
				pkb.is_new=False
				pkb.save()
				acc_piutang=True
				request.session['status']="Data Pelunasan PKB dalam rupiah berhasil diupdate"
		

			if 'pelunasan_piutang_persen' in request.POST:
				pkb = bab3_pkb.objects.get(id_lhe=headerlhe)
				pkb.pelunasan_piutang_persen=request.POST['pelunasan_piutang_persen']
				pkb.is_periode=False
				pkb.is_new=False
				pkb.save()
				acc_piutang=True
				request.session['status']="Data Pelunasan Persentase piutang PKB berhasil diupdate"

			try:
				bulan_awal = request.POST['bulan_awal']
			except:
				bulan_awal=None
			try:
				bulan_akhir = request.POST['bulan_akhir']
			except:
				bulan_akhir=None
			try:
				tahun_awal = int(request.POST['tahun_awal'])
			except:
				tahun_awal=None
			try:
				tahun_akhir = int(request.POST['tahun_akhir'])
			except:
				tahun_akhir=None
			try:
				keterangan = request.POST['keterangan'].strip()
				if len(keterangan)==0:
					keterangan=None
			except:
				keterangan=None

			#request awal
			
			if(bulan_awal!=None and tahun_awal!=None and keterangan!=None):	
				
				if bab3_pkb.objects.filter(id_lhe=headerlhe).count()==0:
					pkb = bab3_pkb()
					pkb.id_lhe = headerlhe
					pkb.bulan_awal=bulan_awal
					pkb.bulan_akhir = bulan_akhir
					pkb.tahun_akhir = tahun_akhir
					pkb.tahun_awal = tahun_awal
					pkb.keterangan= keterangan
					pkb.createdAt = datetime.datetime.now().date()
					pkb.createdBy = request.user.username
					pkb.is_periode=True #true akan menghapus semua data			
					pkb.is_new=True	#akan create awal	
					pkb.save()
					acc_pkb=True
					request.session['status']="Data PKB Berhasil ditambahkan!"
			
			#request update bulan
			if(bulan_awal!=None and tahun_awal==None and keterangan==None):	
				pkb=bab3_pkb.objects.all().get(id_lhe=headerlhe)#.objects.all().filter(id_lhe=headerlhe)
				print(pkb)
				pkb.bulan_awal=bulan_awal
				pkb.bulan_akhir=bulan_akhir
				pkb.createdAt = datetime.datetime.now().date()
				pkb.createdBy = request.user.username
				pkb.is_periode=True #true akan menghapus semua data
				pkb.is_new=False	
				pkb.save()				
				acc_pkb=True
				request.session['status']="Data Periode PKB berhasil diupdate"
			
			#request update tahun
			if(bulan_awal==None and tahun_awal!=None and keterangan==None):	
				pkb=bab3_pkb.objects.all().get(id_lhe=headerlhe)
				pkb.tahun_awal
				pkb.tahun_akhir=tahun_akhir
				pkb.is_periode=False
				pkb.is_new=False	
				pkb.createdAt = datetime.datetime.now().date()
				pkb.createdBy = request.user.username
				pkb.save()
				acc_pkb=True
				request.session['status']="Data Tahun PKB berhasil diupdate"

			#request update keterangan
			if(bulan_awal==None and tahun_awal==None and keterangan!=None):	
				pkb=bab3_pkb.objects.get(id_lhe=headerlhe)
				pkb.keterangan = keterangan
				pkb.is_periode=False
				pkb.createdAt = datetime.datetime.now().date()
				pkb.createdBy = request.user.username
				pkb.is_new=False
				pkb.save()
				acc_pkb=True
				request.session['status']="Data Keterangan PKB berhasil diupdate"

		except Exception as ex:
			request.session['status']="Data Periode PKB gagal ditambahkan/ diubah!"

	try:
		pkb = bab3_pkb.objects.get(id_lhe=headerlhe)
		obj_data_piutang = pkb.obj_data_piutang
		obj_data_piutang_nominal = pkb.obj_data_piutang_nominal
		obj_pelunasan_piutang = pkb.obj_pelunasan_piutang
		obj_pelunasan_piutang_persen = pkb.obj_pelunasan_piutang_persen
		pelunasan_piutang_persen = pkb.pelunasan_piutang_persen
		pelunasan_piutang_rupiah = pkb.pelunasan_piutang_rupiah
		jml_pkb_roda4_angka = pkb.jml_pkb_roda4
		jml_pkb_kuning_angka = pkb.jml_pkb_kuning
		jml_pkb_hitam_angka = pkb.jml_pkb_hitam
		jml_pkb_roda4_huruf = konversi_angka(jml_pkb_roda4_angka)
		jml_pkb_kuning_huruf = konversi_angka(jml_pkb_kuning_angka)
		jml_pkb_hitam_huruf = konversi_angka(jml_pkb_hitam_angka)
		penelitian_ulang = pkb.penelitian_ulang		
		pkb_detail = bab3_pkb_detail.objects.all().filter(id_pkb=pkb)
	
	except Exception as ex:
		print(ex)
		print('get headerlhe')
		pkb=None
		pkb_detail=None
			
	lokasi = headerlhe.suratTugas.lokasi
	forms = inputBab3PKB

	try:
		keterangan = pkb.keterangan
	except:
		keterangan=None
	# jml_pkb_roda4 = models.IntegerField(default=0,blank=True,null=True)
    # jml_pkb_kuning = models.IntegerField(default=0,blank=True,null=True)
    # jml_pkb_hitam = models.IntegerField(default=0,blank=True,null=True)
    
	
	try:
		tahun_awal = pkb.tahun_awal
	except:
		tahun_awal=None
	try:
		tahun_akhir = pkb.tahun_akhir
	except:
		tahun_akhir=None
	try:
		bulan_awal = konversi_bulan(pkb.bulan_awal)
	except:
		bulan_awal=None
	try:
		bulan_akhir = konversi_bulan(pkb.bulan_akhir)
	except:
		bulan_akhir=None
	try:
		selisih_angka = pkb_detail.aggregate(Sum('selisih_angka'))['selisih_angka__sum']
	except:
		selisih_angka=0
	try:
		total_tahun_awal = pkb_detail.aggregate(Sum('nilai_awal'))['nilai_awal__sum']
		selisih_persen = selisih_angka/total_tahun_awal
	except:
		selisih_persen=0
	try:
		total_tahun_awal = pkb_detail.aggregate(Sum('nilai_awal'))['nilai_awal__sum']
	except:
		total_tahun_awal = 0
	try:
		total_tahun_akhir = pkb_detail.aggregate(Sum('nilai_akhir'))['nilai_akhir__sum']
	except:
		total_tahun_akhir=0
	
	statusnya = request.session['status']
	request.session['status']=""

	context = {
		'nomor_lhe':headerlhe.nomor_lhe,
		'id_lhe':headerlhe.id_lhe,
		'forms':forms,
		'lokasi':lokasi,
		'tahun_awal':tahun_awal,
		'tahun_akhir':tahun_akhir,
		'bulan_awal':bulan_awal,
		'bulan_akhir':bulan_akhir,
		'selisih_angka':selisih_angka,
		'selisih_persen':selisih_persen,
		'total_tahun_awal':total_tahun_awal,
		'total_tahun_akhir':total_tahun_akhir,
		'pkb_detail':pkb_detail,
		'pending_surat':getPendingSurat(),
		'pending_lhe':getPendingLHE(),
		'keterangan': keterangan,
		'acc_pkb':acc_pkb,
		'acc_piutang':acc_piutang,
		'obj_data_piutang':obj_data_piutang,
		'obj_data_piutang_nominal':obj_data_piutang_nominal,
		'obj_pelunasan_piutang':obj_pelunasan_piutang,
		'obj_pelunasan_piutang_persen':obj_pelunasan_piutang_persen,
		'pelunasan_piutang_persen':pelunasan_piutang_persen,
		'pelunasan_piutang_rupiah':pelunasan_piutang_rupiah,
		'acc_penetapan':acc_penetapan,
		'jml_pkb_roda4_angka':jml_pkb_roda4_angka,
		'jml_pkb_kuning_angka':jml_pkb_kuning_angka,
		'jml_pkb_hitam_angka':jml_pkb_hitam_angka,
		'jml_pkb_roda4_huruf':jml_pkb_roda4_huruf,
		'jml_pkb_kuning_huruf':jml_pkb_kuning_huruf,
		'jml_pkb_hitam_huruf':jml_pkb_hitam_huruf,
		'penelitian_ulang':penelitian_ulang,
		'status':statusnya
	}

	return render(request,'lhe/create_lhe_bab2_c_pkb.html',context)

def updatePKBDetail(request,id,id_update):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	
	id_pkb_detail = bab3_pkb_detail.objects.get(id_pkb_detail=id_update)
	id_pkb_detail.nilai_awal=int(request.POST['nilai_awal_new'])
	id_pkb_detail.nilai_akhir=int(request.POST['nilai_akhir_new'])
	id_pkb_detail.save()
	request.session['status']="Data PKB Berhasil diupdate!"

	return HttpResponseRedirect(f'/lhe/add/b2/pkb/{id}/')

def addLHE_b2_bbnkb(request,id):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')

	headerlhe = headerLHE.objects.get(id_lhe=id)
		
	if request.method == "POST":
		#apakah update piutang?
		#cek dolo
		try:
			try:
				bulan_awal = request.POST['bulan_awal']
			except:
				bulan_awal=None
			try:
				bulan_akhir = request.POST['bulan_akhir']
			except:
				bulan_akhir=None
			try:
				tahun_awal = int(request.POST['tahun_awal'])
			except:
				tahun_awal=None
			try:
				tahun_akhir = int(request.POST['tahun_akhir'])
			except:
				tahun_akhir=None
			try:
				keterangan = request.POST['keterangan'].strip()
				if len(keterangan)==0:
					keterangan=None
			except:
				keterangan=None

			#request awal
			
			if(bulan_awal!=None and tahun_awal!=None and keterangan!=None):	
				if bab3_bbnkb.objects.filter(id_lhe=headerlhe).count()==0:
					bnkb = bab3_bbnkb()
					bnkb.id_lhe = headerlhe
					bnkb.bulan_awal=bulan_awal
					bnkb.bulan_akhir = bulan_akhir
					bnkb.tahun_akhir = tahun_akhir
					bnkb.tahun_awal = tahun_awal
					bnkb.keterangan= keterangan
					bnkb.createdAt = datetime.datetime.now().date()
					bnkb.createdBy = request.user.username
					bnkb.is_periode=True #true akan menghapus semua data			
					bnkb.is_new=True	#akan create awal	
					bnkb.save()
			
			#request update bulan
			if(bulan_awal!=None and tahun_awal==None and keterangan==None):	
				bnkb=bab3_bbnkb.objects.all().get(id_lhe=headerlhe)#.objects.all().filter(id_lhe=headerlhe)
				bnkb.bulan_awal=bulan_awal
				bnkb.bulan_akhir=bulan_akhir
				bnkb.createdAt = datetime.datetime.now().date()
				bnkb.createdBy = request.user.username
				bnkb.is_periode=True #true akan menghapus semua data
				bnkb.is_new=False	
				bnkb.save()				
			
			#request update tahun
			if(bulan_awal==None and tahun_awal!=None and keterangan==None):	
				bnkb=bab3_bbnkb.objects.all().get(id_lhe=headerlhe)
				bnkb.tahun_awal=tahun_awal
				bnkb.tahun_akhir=tahun_akhir
				bnkb.is_periode=False
				bnkb.is_new=False	
				bnkb.createdAt = datetime.datetime.now().date()
				bnkb.createdBy = request.user.username
				bnkb.save()

			#request update keterangan
			if(bulan_awal==None and tahun_awal==None and keterangan!=None):	
				bnkb=bab3_bbnkb.objects.get(id_lhe=headerlhe)
				bnkb.keterangan = keterangan
				bnkb.is_periode=False
				bnkb.createdAt = datetime.datetime.now().date()
				bnkb.createdBy = request.user.username
				bnkb.is_new=False
				bnkb.save()

		except Exception as ex:
			print(ex)
			print('error post')

	try:
		bnkb = bab3_bbnkb.objects.get(id_lhe=headerlhe)
		bnkb_detail = bab3_bbnkb_detail.objects.all().filter(id_bbnkb=bnkb)
	
	except Exception as ex:
		print(ex)
		print('get headerlhe')
		bnkb=None
		bnkb_detail=None
			
	lokasi = headerlhe.suratTugas.lokasi
	forms = inputBab3BNKB

	try:
		keterangan = bnkb.keterangan
	except:
		keterangan=None
	# jml_pkb_roda4 = models.IntegerField(default=0,blank=True,null=True)
    # jml_pkb_kuning = models.IntegerField(default=0,blank=True,null=True)
    # jml_pkb_hitam = models.IntegerField(default=0,blank=True,null=True)
    
	
	try:
		tahun_awal = bnkb.tahun_awal
	except:
		tahun_awal=None
	try:
		tahun_akhir = bnkb.tahun_akhir
	except:
		tahun_akhir=None
	try:
		bulan_awal = konversi_bulan(bnkb.bulan_awal)
	except:
		bulan_awal=None
	try:
		bulan_akhir = konversi_bulan(bnkb.bulan_akhir)
	except:
		bulan_akhir=None
	try:
		selisih_angka = bnkb_detail.aggregate(Sum('selisih_angka'))['selisih_angka__sum']
	except:
		selisih_angka=0
	try:
		total_tahun_awal = bnkb_detail.aggregate(Sum('nilai_awal'))['nilai_awal__sum']
		selisih_persen = selisih_angka/total_tahun_awal
	except:
		selisih_persen=0
	try:
		total_tahun_awal = bnkb_detail.aggregate(Sum('nilai_awal'))['nilai_awal__sum']
	except:
		total_tahun_awal = 0
	try:
		total_tahun_akhir = bnkb_detail.aggregate(Sum('nilai_akhir'))['nilai_akhir__sum']
	except:
		total_tahun_akhir=0

	statusnya = request.session['status']
	request.session['status']=""
	

	context = {
		'nomor_lhe':headerlhe.nomor_lhe,
		'id_lhe':headerlhe.id_lhe,
		'forms':forms,
		'lokasi':lokasi,
		'tahun_awal':tahun_awal,
		'tahun_akhir':tahun_akhir,
		'bulan_awal':bulan_awal,
		'bulan_akhir':bulan_akhir,
		'selisih_angka':selisih_angka,
		'selisih_persen':selisih_persen,
		'total_tahun_awal':total_tahun_awal,
		'total_tahun_akhir':total_tahun_akhir,
		'bnkb_detail':bnkb_detail,
		'pending_surat':getPendingSurat(),
		'pending_lhe':getPendingLHE(),
		'keterangan': keterangan,
		'status':statusnya
	}
	return render(request,'lhe/create_lhe_bab2_c_bnkb.html',context)

def updateBBNKBDetail(request,id,id_update):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	id_bbnkb_detail = bab3_bbnkb_detail.objects.get(id_bbnkb_detail=id_update)
	id_bbnkb_detail.nilai_awal=int(request.POST['nilai_awal_new'])
	id_bbnkb_detail.nilai_akhir=int(request.POST['nilai_akhir_new'])
	id_bbnkb_detail.save()

	return HttpResponseRedirect(f'/lhe/add/b2/bbnkb/{id}/')

def addLHE_b2_pap(request,id):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')

	headerlhe = headerLHE.objects.get(id_lhe=id)

	statusnya = request.session['status']
	try:
		pembayaran = request.session['pembayaran']
		print('ini pembayaran')
		request.session['pembayaran']=False
	except:
		print('bukan pembayaran')
		pembayaran = False
	if request.method=="POST":
		if(pembayaran !=True):
			if('tahun1' in request.POST and 'tahun2' in request.POST and 'jml_obj_spbu' in request.POST):
				if(int(request.POST['bulan1_awal'])<int(request.POST['bulan1_akhir'])  and int(request.POST['bulan2_awal'])<int(request.POST['bulan2_akhir'])):
					pap = bab3_pap()
					pap.id_lhe = headerlhe
					pap.bulan1_akhir = int(request.POST['bulan1_akhir'])
					pap.bulan1_awal = int(request.POST['bulan1_awal'])
					pap.tahun1 = int(request.POST['tahun1'])
					pap.bulan2_akhir = int(request.POST['bulan2_akhir'])
					pap.bulan2_awal = int(request.POST['bulan2_awal'])
					pap.tahun2 = int(request.POST['tahun2'])
					pap.jml_obj_pap_berijin = int(request.POST['jml_obj_pap_berijin'])
					pap.jml_obj_pap_nonijin = int(request.POST['jml_obj_pap_nonijin'])
					pap.jml_obj_spbu=int(request.POST['jml_obj_spbu'])
					pap.createdBy = request.user.username
					pap.createdAt = datetime.datetime.now()
					pap.is_new = True
					try:
						pap.save()
						request.session['status']="Data PAP berhasil ditambahkan!"
					except:
						request.session['status']="Data PAP gagal ditambahkan karena sudah ada sebelumnya!"
				else:	
					request.session['status']="Data PAP gagal ditambahkan! Bulan Awal harus lebih kecil dari Bulan Akhir!"

			elif('tahun1' in request.POST and 'bulan1_awal' in request.POST):
				print(f"statusnya: {request.session['status']}")
				try:
					if(int(request.POST['bulan1_awal'])<int(request.POST['bulan1_akhir'])):
						pap = bab3_pap.objects.get(id_lhe=headerlhe)
						pap.tahun1 = int(request.POST['tahun1'])
						pap.bulan1_awal = int(request.POST['bulan1_awal'])
						pap.bulan1_akhir = int(request.POST['bulan1_akhir'])
						pap.createdAt = datetime.datetime.now()
						pap.createdBy = request.user.username
						pap.is_periode1=True
						pap.save()
						request.session['status']="Update Periode Pertama Berhasil!"
					else:
						request.session['status']="Update Periode Pertama Gagal! Perhatikan Bulan Awal harus lebih kecil dari Bulan Akhir!"
				except Exception as ex:
					print(ex)
					request.session['status']="Update Periode Pertama Gagal!"
			
			elif('tahun2' in request.POST and 'bulan2_awal' in request.POST):
				try:
					if(int(request.POST['bulan2_awal'])<int(request.POST['bulan2_akhir'])):
						pap = bab3_pap.objects.get(id_lhe=headerlhe)
						pap.tahun2 = int(request.POST['tahun2'])
						pap.bulan2_awal = int(request.POST['bulan2_awal'])
						pap.bulan2_akhir = int(request.POST['bulan2_akhir'])
						pap.createdAt = datetime.datetime.now()
						pap.createdBy = request.user.username
						pap.is_periode2=True
						pap.save()
						request.session['status']="Update Periode Kedua Berhasil!"
					else:
						request.session['status']="Update Periode Kedua Gagal! Perhatikan Bulan Awal harus lebih kecil dari Bulan Akhir!"
				except:
					request.session['status']="Update Periode Kedua Gagal!"
			
			elif('jml_obj_pap_berijin' in request.POST):
				try:
						pap = bab3_pap.objects.get(id_lhe=headerlhe)
						pap.jml_obj_pap_berijin = int(request.POST['jml_obj_pap_berijin'])
						pap.createdAt = datetime.datetime.now()
						pap.createdBy = request.user.username
						pap.is_obj=True
						pap.save()
						request.session['status']="Update Jumlah PAP Berijin Berhasil!"
				except:
					request.session['status']="Update Jumlah PAP Berijin Gagal!"

			elif('jml_obj_pap_nonijin' in request.POST):
				try:
						pap = bab3_pap.objects.get(id_lhe=headerlhe)
						pap.jml_obj_pap_nonijin = int(request.POST['jml_obj_pap_nonijin'])
						pap.createdAt = datetime.datetime.now()
						pap.createdBy = request.user.username
						pap.is_obj=True
						pap.save()
						request.session['status']="Update Jumlah PAP Tidak Berijin Berhasil!"
				except:
					request.session['status']="Update Jumlah PAP Tidak Berijin Gagal!"

			elif('jml_obj_spbu' in request.POST):
				try:
						pap = bab3_pap.objects.get(id_lhe=headerlhe)
						pap.jml_obj_spbu = int(request.POST['jml_obj_spbu'])
						pap.createdAt = datetime.datetime.now()
						pap.createdBy = request.user.username
						pap.is_obj=True
						pap.save()
						request.session['status']="Update Jumlah SPBU Berhasil!"
				except:
					request.session['status']="Update Jumlah SPBU Gagal!"
			
			elif('keterangan' in request.POST):
				try:
						pap = bab3_pap.objects.get(id_lhe=headerlhe)
						pap.keterangan = request.POST['keterangan']
						pap.createdAt = datetime.datetime.now()
						pap.createdBy = request.user.username
						pap.is_obj=True
						pap.save()
						request.session['status']="Update Simpulan Analisa Berhasil!"
				except:
					request.session['status']="Update Simpulan Analisa Gagal!"

	forms = inputBab3PAP()

	try:
		mypap = bab3_pap.objects.get(id_lhe=headerlhe)
		mypap_tahun1 = bab3_pap_tahun1.objects.all().filter(id_pap=mypap)
		mypap_tahun2 = bab3_pap_tahun2.objects.all().filter(id_pap=mypap)
	except:
		mypap = None
		mypap_tahun1 = None
		mypap_tahun2 = None

	request.session['status']=""
	
	try:
		persen_tahun1 = f"{mypap.selisih_tahun1_persen*100:.2f}"
	except:
		persen_tahun1 = "0.00"
	try:
		persen_tahun2 = f"{mypap.selisih_tahun2_persen*100:.1f}"
	except:
		persen_tahun2 = "0.00"
	try:
		over_tahun1 = int(mypap.selisih_tahun1_persen-1*100)
	except:
		over_tahun1 = 0
	context = {
		'nomor_lhe':headerlhe.nomor_lhe,
		'id_lhe':headerlhe.id_lhe,
		'forms':forms,
		'mypap':mypap,
		'mypap_tahun1':mypap_tahun1,
		'mypap_tahun2':mypap_tahun2,
		'status':statusnya,
		'pending_surat':getPendingSurat(),
		'pending_lhe':getPendingLHE(),
		'persen_tahun1':persen_tahun1,
		'persen_tahun2':persen_tahun2,
		'over_tahun1':over_tahun1
		# 'lokasi':lokasi,
		# 'tahun_awal':tahun_awal,
		# 'tahun_akhir':tahun_akhir,
		# 'bulan_awal':bulan_awal,
		# 'bulan_akhir':bulan_akhir,
		# 'selisih_angka':selisih_angka,
		# 'selisih_persen':selisih_persen,
		# 'total_tahun_awal':total_tahun_awal,
		# 'total_tahun_akhir':total_tahun_akhir,
		# 'bnkb_detail':bnkb_detail,
		# 'pending_surat':getPendingSurat(),
		# 'pending_lhe':getPendingLHE(),
		# 'keterangan': keterangan,
	}

	return render(request,'lhe/create_lhe_bab2_c_pap.html',context)

def updatePAP_tahun1(request,id,id_update):
	if(request.user.is_authenticated != True):
			return HttpResponseRedirect('/auth/')
	try:
		pap_tahun1 = bab3_pap_tahun1.objects.get(id_pap_tahun1=id_update)
		pap_tahun1.pembayaran = int(request.POST['pembayaran'])
		pap_tahun1.penetapan = int(request.POST['penetapan'])
		pap_tahun1.selisih_angka = int(request.POST['pembayaran']) - int(request.POST['penetapan'])
		if(int(request.POST['pembayaran']) - int(request.POST['penetapan']) == 0):
			pap_tahun1.selisih_persen=0
		else:
			pap_tahun1.selisih_persen= (int(request.POST['pembayaran']) - int(request.POST['penetapan']))/int(request.POST['penetapan'])
		pap_tahun1.save()
		request.session['status']='Update Pembayaran dan Penetapan Tahun Pertama Berhasil!'	
	except Exception as ex:
		request.session['status']='Update Pembayaran dan Penetapan Tahun Pertama Gagal!'
	request.session['pembayaran']=True
	return HttpResponseRedirect(f'/lhe/add/b2/pap/{id}/')

def updatePAP_tahun2(request,id,id_update):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	try:
		pap_tahun2 = bab3_pap_tahun2.objects.get(id_pap_tahun2=id_update)
		pap_tahun2.pembayaran = int(request.POST['pembayaran'])
		pap_tahun2.penetapan = int(request.POST['penetapan'])
		# print(pap_tahun2)
		pap_tahun2.selisih_angka = int(request.POST['pembayaran']) - int(request.POST['penetapan'])
		if(int(request.POST['pembayaran']) - int(request.POST['penetapan']) == 0):
			pap_tahun2.selisih_persen=0
		else:
			pap_tahun2.selisih_persen= (int(request.POST['pembayaran']) - int(request.POST['penetapan']))/int(request.POST['penetapan'])
		pap_tahun2.save()
		request.session['status']='Update Pembayaran dan Penetapan Tahun Kedua Berhasil!'	
	except Exception as ex:
		print(ex)
		request.session['status']='Update Pembayaran dan Penetapan Tahun Kedua Gagal!'
	request.session['pembayaran']=True
	return HttpResponseRedirect(f'/lhe/add/b2/pap/{id}/')
from django.shortcuts import render, HttpResponseRedirect
from cms.forms import inputGolongan, inputJabatan, inputPegawai, inputPengguna
from surat_tugas.models import MasterGolongan,MasterJabatan,MasterPegawai, Pengguna, Logging
from django.core.paginator import Paginator
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q

def addLogging(username,grouping,message):
	loggingnya=Logging.objects.create(
		user=Pengguna.objects.get(username=username),
		transaction=message,
		grouping=grouping
	)
	return loggingnya


def dashboard(request):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')

	context={
		'menuname':'Dashboard',
		'pathway': '',
		'username': request.user.username
	}
	return render(request,'master/dashboard.html',context)

def addGolongan(request):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	if request.method=="POST":
		kode_golongan = request.POST['kode_golongan']
		keterangan = request.POST['keterangan']

		try:
			golongan = MasterGolongan.objects.create(
				kode_golongan=kode_golongan,
				keterangan=keterangan,
				updatedBy=request.user.username
			)
			golongan.save()
			addLogging(request.user.username,"master_golongan",f"create kode: {kode_golongan} - {keterangan}" )
		except:
			pass

	context={
		'forms':inputGolongan,
		'menuname':'Menambah Golongan',
		'pathway':'Master Golongan - Menambah Golongan',
		'username': request.user.username
	}
	return render(request,'master/create_golongan.html',context)

def displayGolongan(request):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	try:
		page=request.GET['page']
	except:
		page=1
	if page==None:
		page=1
	listGolongan = MasterGolongan.objects.all().order_by('-updatedAt')
	p=Paginator(listGolongan,5)
	
	try:
		halaman = p.page(page)
	except:
		halaman = p.page(1)
	context={
		'lists':halaman,
		'paginator':p,
		'menuname':'Daftar Golongan',
		'pathway':'Master Golongan - Daftar Golongan',
		'username':request.user.username,
		'mywebsite': '/master/gol/dis/'
	}
	return render(request,'master/display_golongan.html',context)


def addJabatan(request):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	if request.method=="POST":
		kode_jabatan = request.POST['kode_jabatan']
		keterangan = request.POST['keterangan']

		try:
			jabatan = MasterJabatan.objects.create(
				kode_jabatan=kode_jabatan,
				keterangan=keterangan,
				updatedBy=request.user.username
			)
			jabatan.save()
			addLogging(request.user.username,"master_jabatan",f"create kode: {kode_jabatan} - {keterangan}" )
		except:
			pass


	context={
		'forms':inputJabatan,
		'menuname':'Menambah Jabatan',
		'pathway':'Master Jabatan - Menambah Jabatan',
		'username':request.user.username
	}
	return render(request,'master/create_jabatan.html',context)

def displayJabatan(request):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	try:
		page=request.GET['page']
	except:
		page=1
	if page==None:
		page=1

	listJabatan = MasterJabatan.objects.all().order_by('-updatedAt')
	
	p=Paginator(listJabatan,5)
	
	
	try:
		halaman = p.page(page)
	except:
		halaman = p.page(1)
	
	context={
		'lists':halaman,
		'paginator':p,
		'menuname':'Daftar Jabatan',
		'pathway':'Master Jabatan - Daftar Jabatan',
		'username':request.user.username,
		'mywebsite': '/master/jab/dis/'
	}
	return render(request,'master/display_jabatan.html',context)

def delGolongan(request,id):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	try:
		MasterGolongan.objects.filter(kode_golongan=id).delete()
		addLogging(request.user.username,"master_golongan",f"delete kode: {id}" )
	except:
		pass
	return HttpResponseRedirect('/master/gol/dis/')

def delJabatan(request,id):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	try:
		MasterJabatan.objects.filter(kode_jabatan=id).delete()
		addLogging(request.user.username,"master_jabatan",f"delete kode: {id}" )
	except:
		pass
	return HttpResponseRedirect('/master/jab/dis/')

def addPegawai(request):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	if request.method=="POST":
		nik = request.POST['nik']
		nama = request.POST['nama']
		kode_jabatan = request.POST['kode_jabatan']
		kode_golongan = request.POST['kode_golongan']
		try:
			is_kepala = request.POST['is_kepala']
			is_kepala=True
		except:
			is_kepala=False

		try:
			jabatan = MasterPegawai.objects.create(
				nik = nik,
				nama=nama,
				kode_jabatan=MasterJabatan.objects.get(kode_jabatan=kode_jabatan),
				kode_golongan=MasterGolongan.objects.get(kode_golongan=kode_golongan),
				is_kepala=is_kepala,
				updatedBy=request.user.username
			)
			jabatan.save()
			addLogging(request.user.username,"master_pegawai",f"create NIP: {nik} - {nama}" )
		except:
			pass
	context={
		'forms':inputPegawai,
		'menuname':'Menambah Pegawai',
		'pathway':'Master Pegawai - Menambah Pegawai',
		'username':request.user.username
	}
	return render(request,'master/create_pegawai.html',context)

def displayPegawai(request):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	try:
		page=request.GET['page']
	except:
		page=1
	if page==None:
		page=1

	listPegawai = MasterPegawai.objects.all().order_by('-updatedAt')
	
	p=Paginator(listPegawai,5)
	
	
	try:
		halaman = p.page(page)
	except:
		halaman = p.page(1)
	
	context={
		'lists':halaman,
		'paginator':p,
		'menuname':'Daftar Pegawai',
		'pathway':'Master Pegawai - Daftar Pegawai',
		'username':request.user.username,
		'mywebsite': '/master/peg/dis/'
	}
	return render(request,'master/display_pegawai.html',context)

def delPegawai(request,id):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	try:
		MasterPegawai.objects.filter(nik=id).delete()
		addLogging(request.user.username,"master_pegawai",f"delete kode: {id}" )
	except:
		pass
	return HttpResponseRedirect('/master/peg/dis/')

def addPengguna(request):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		email = request.POST['username']
		try:
			is_create = request.POST['is_create']
			is_create = True
		except:
			is_create=False

		try:
			is_edit = request.POST['is_edit']
			is_edit = True
		except:
			is_edit=False

		try:
			is_delete = request.POST['is_delete']
			is_delete = True
		except:
			is_delete=False

		try:
			pengguna = Pengguna.objects.create(
				username=username,
				password=password,
				email=email,
				is_create=is_create,
				is_edit=is_edit,
				is_delete=is_delete,
				updatedBy=request.user.username
			)
			pengguna.save()
			pengguna=Pengguna.objects.get(username=username)
			pengguna.set_password(password)
			pengguna.save()
			addLogging(request.user.username,"master_pengguna",f"create username: {username} - {email}" )
		except:
			pass

	context={
		'forms':inputPengguna,
		'menuname':'Menambah Pengguna Aplikasi',
		'pathway':'Master Pengguna - Menambah Pengguna',
		'username':request.user.username
	}
	return render(request,'master/create_pengguna.html',context)

def displayPengguna(request):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	try:
		page=request.GET['page']
	except:
		page=1
	if page==None:
		page=1

	listPengguna = Pengguna.objects.all().order_by('-updatedAt')
	
	p=Paginator(listPengguna,5)
	
	
	try:
		halaman = p.page(page)
	except:
		halaman = p.page(1)
	
	context={
		'lists':halaman,
		'paginator':p,
		'menuname':'Daftar Pengguna Aplikasi',
		'pathway':'Master Pengguna - Daftar Pengguna',
		'username':request.user.username,
		'mywebsite': '/master/user/dis/'
	}
	return render(request,'master/display_pengguna.html',context)

def delPengguna(request,id):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	try:
		Pengguna.objects.filter(username=id).delete()
		addLogging(request.user.username,"master_pengguna",f"delete kode: {id}" )
	except:
		pass
	return HttpResponseRedirect('/master/user/dis/')

def loginuser(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user = authenticate(username=username,password=password)
		if(user != None):
			login(request,user)
			if(request.user.is_authenticated):
				addLogging(request.user.username,"login",f"berhasil" )
			return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/auth/')
		
	if(request.user.is_authenticated):
		return HttpResponseRedirect('/')
	else:
		return render(request,'login.html')


def logoutuser(request):
	addLogging(request.user.username,"logout",f"berhasil" )
	logout(request)
	return HttpResponseRedirect('/auth/')

def displayLog(request):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	if(request.user.is_superuser !=True):
		return HttpResponseRedirect('/')
	
	#get the parameters query 
	print(request.GET.dict())

	try:
		page=request.GET['page']
	except:
		page=1
	if page==None:
		page=1

	listLogging = Logging.objects.all().order_by('-updatedAt')
	
	p=Paginator(listLogging,10)
	
	
	try:
		halaman = p.page(page)
	except:
		halaman = p.page(1)
	
	context={
		'lists':halaman,
		'paginator':p,
		'menuname':'Daftar Log User',
		'pathway':'log transaksi',
		'username':request.user.username
	}
	return render(request,'master/display_logging.html',context)

def displayGolonganID(request,id):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	try:
		page=request.GET['page']
	except:
		page=1
	if page==None:
		page=1
	listGolongan = MasterGolongan.objects.all().filter(Q(kode_golongan__icontains=id) | Q(keterangan__icontains=id)).order_by('-updatedAt')
	p=Paginator(listGolongan,5)
	
	try:
		halaman = p.page(page)
	except:
		halaman = p.page(1)
	context={
		'lists':halaman,
		'paginator':p,
		'menuname':'Daftar Golongan  [' + str(id).upper() + "]",
		'pathway':'Master Golongan - Daftar Golongan',
		'username':request.user.username,
		'mywebsite': '/master/gol/dis/'
	}
	return render(request,'master/display_golongan.html',context)

def displayJabatanID(request,id):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	try:
		page=request.GET['page']
	except:
		page=1
	if page==None:
		page=1
	listJabatan = MasterJabatan.objects.all().filter(Q(kode_jabatan__icontains=id) | Q(keterangan__icontains=id)).order_by('-updatedAt')
	p=Paginator(listJabatan,5)
	
	try:
		halaman = p.page(page)
	except:
		halaman = p.page(1)
	context={
		'lists':halaman,
		'paginator':p,
		'menuname':'Daftar Jabatan  [' + str(id).upper() + "]",
		'pathway':'Master Jabatan - Daftar Jabatan',
		'username':request.user.username,
		'mywebsite': '/master/jab/dis/'
	}
	return render(request,'master/display_jabatan.html',context)

def displayPegawaiID(request,id):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	try:
		page=request.GET['page']
	except:
		page=1
	if page==None:
		page=1
	listPegawai = MasterPegawai.objects.all().filter(Q(nik__icontains=id) | Q(nama__icontains=id)).order_by('-updatedAt')
	p=Paginator(listPegawai,5)
	
	try:
		halaman = p.page(page)
	except:
		halaman = p.page(1)
	context={
		'lists':halaman,
		'paginator':p,
		'menuname':'Daftar Pegawai  [' + str(id).upper() + "]",
		'pathway':'Master Pegawai - Daftar Pegawai',
		'username':request.user.username,
		'mywebsite': '/master/peg/dis/'
	}
	return render(request,'master/display_pegawai.html',context)

def displayPenggunaID(request,id):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	try:
		page=request.GET['page']
	except:
		page=1
	if page==None:
		page=1
	listPengguna = Pengguna.objects.all().filter(Q(username__icontains=id) | Q(email__icontains=id)).order_by('-updatedAt')
	p=Paginator(listPengguna,5)
	
	try:
		halaman = p.page(page)
	except:
		halaman = p.page(1)
	context={
		'lists':halaman,
		'paginator':p,
		'menuname':'Daftar Pengguna Aplikasi  [' + str(id).upper() + "]",
		'pathway':'Master Pengguna - Daftar Pengguna',
		'username':request.user.username,
		'mywebsite': '/master/user/dis/'
	}
	return render(request,'master/display_pengguna.html',context)

def displayLogID(request,id):
	if(request.user.is_authenticated != True):
		return HttpResponseRedirect('/auth/')
	if(request.user.is_superuser !=True):
		return HttpResponseRedirect('/')
	
	#get the parameters query 
	print(request.GET.dict())

	try:
		page=request.GET['page']
	except:
		page=1
	if page==None:
		page=1

	listLogging = Logging.objects.all().filter(Q(grouping__icontains=id) | Q(transaction__icontains=id)).order_by('-updatedAt')
	
	p=Paginator(listLogging,10)
	
	
	try:
		halaman = p.page(page)
	except:
		halaman = p.page(1)
	
	context={
		'lists':halaman,
		'paginator':p,
		'menuname':'Daftar Log User ['+str(id).upper()+']',
		'pathway':'log transaksi',
		'username':request.user.username,
		'mywebsite': '/logs/'

	}
	return render(request,'master/display_logging.html',context)
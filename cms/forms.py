from django import forms
from surat_tugas.models import MasterGolongan, MasterJabatan, MasterPegawai, Pengguna, TrxSuratTugas
from bootstrap_datepicker_plus.widgets import DatePickerInput
from surat_tugas.models import ST_DasarTugas, ST_Peserta, MasterDasarST



class inputGolongan(forms.ModelForm):
	class Meta:
		model = MasterGolongan
		fields = ['kode_golongan','keterangan']

		widgets= {
			'kode_golongan': forms.TextInput(
				attrs={'required':'required'}),
			'keterangan':forms.TextInput(attrs={'required':'required'})
		}

class inputJabatan(forms.ModelForm):
	class Meta:
		model = MasterJabatan
		fields = ['kode_jabatan','keterangan']

		widgets= {
			'kode_golongan': forms.TextInput(attrs={'required':'required'}),
			'keterangan':forms.TextInput(attrs={'required':'required'})
		}

class inputPegawai(forms.ModelForm):
	class Meta:
		model = MasterPegawai
		fields = ['nik','nama','kode_jabatan','kode_golongan','is_kepala']

		widgets= {
			'nik': forms.TextInput(attrs={'required':'required'}),
			'nama':forms.TextInput(attrs={'required':'required'}),
			'kode_jabatan': forms.Select(attrs={'required':'required'}),
			'kode_golongan':forms.Select(attrs={'required':'required'})
		}

class inputPengguna(forms.ModelForm):
	class Meta:
		model = Pengguna
		fields = ['username','password','email','is_create','is_edit','is_delete']

		widgets= {
			'username': forms.TextInput(attrs={'required':'required'}),
			'password':forms.TextInput(attrs={'required':'required','type':'password'}),
			'email': forms.TextInput(attrs={'required':'required','type':'email'}),
		}

class inputSuratTugas(forms.ModelForm):
	class Meta:
		model = TrxSuratTugas
		fields = ['nomor_surat','tgl_surat','lokasi_surat','tujuan','lokasi','tgl_awal_tugas',
			'tgl_akhir_tugas']

		widgets= {
			'nomor_surat': forms.TextInput(attrs={'required':'required','placeholder':'Nomor surat','class':'form-control'}),
			'lokasi_surat': forms.TextInput(attrs={'required':'required','placeholder':'Tempat dibuat surat','class':'form-control'}),
			'tgl_surat': DatePickerInput(attrs={'required':'required','class':'form-control'}),#forms.DateInput(attrs={'id':'tgl_surat','required':'required','class':'form-control'}),
			'tujuan': forms.TextInput(attrs={'required':'required','placeholder':'Tujuan Penugasan','class':'form-control'}),
			'lokasi': forms.TextInput(attrs={'required':'required','placeholder':'Lokasi Penugasan','class':'form-control'}),
			'tgl_awal_tugas':DatePickerInput(attrs={'required':'required','class':'form-control'}), #(attrs={'id':'tgl_awal_tugas','required':'required','class':'form-control'}),
			'tgl_akhir_tugas': DatePickerInput(attrs={'required':'required','class':'form-control'})#forms.DateInput(attrs={'id':'tgl_akhir_tugas','required':'required','class':'form-control'})
			
		}

class inputMasterDasarST(forms.ModelForm):
	class Meta:
		model = MasterDasarST
		fields = ['kode_dasar','keterangan']

		widgets= {
			'kode_dasar': forms.TextInput(attrs={'required':'required','placeholder':'kode dasar surat tugas','class':'form-control'}),
			'keterangan': forms.TextInput(attrs={'required':'required','placeholder':'kode dasar surat tugas','class':'form-control'})
		}
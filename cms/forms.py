from django import forms
from surat_tugas.models import MasterGolongan, MasterJabatan, MasterPegawai, Pengguna


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

from django import forms
from lhe.models import headerLHE, bab2_tatausaha_kepegawaian_normatif, bab3_pkb, bab3_bbnkb
from surat_tugas.models import TrxSuratTugas
from bootstrap_datepicker_plus.widgets import DatePickerInput

class inputHeaderLHE(forms.ModelForm):
	class Meta:
		model = headerLHE
		fields = ['suratTugas','nomor_lhe','tanggal_lhe']

		widgets = {
			'suratTugas': forms.Select(attrs={'class':'form-control'}),
			'nomor_lhe':forms.TextInput(attrs={'required':'required','class':'form-control','placeholder':'Nomor LHE'}),
			'tanggal_lhe':DatePickerInput(attrs={'required':'required','class':'form-control','placeholder':'Tanggal Buat LHE'})
		}
		
	def __init__(self,*args,**kwargs):
		super(inputHeaderLHE,self).__init__(**kwargs)
		self.fields['suratTugas'].queryset = TrxSuratTugas.objects.all().filter(submit=True,is_lhe=False)

class inputNormatifLHE(forms.ModelForm):
	class Meta:
		model = bab2_tatausaha_kepegawaian_normatif
		fields = ['nama','nip','jabatan']

		widgets = {
			'jabatan': forms.Select(attrs={'class':'form-control'}),
			'nama':forms.TextInput(attrs={'required':'required','class':'form-control','placeholder':'Nama Pegawai'}),
			'nip':forms.TextInput(attrs={'required':'required','class':'form-control','placeholder':'N.I.P Pegawai'})
		}


class inputBab3PKB(forms.ModelForm):
	class Meta:
		model = bab3_pkb
		fields = ['bulan_awal','bulan_akhir','tahun_awal','tahun_akhir','keterangan']

		widgets = {
			'bulan_awal': forms.Select(attrs={'class':'form-control'}),
			'bulan_akhir': forms.Select(attrs={'class':'form-control'}),
			'tahun_awal':forms.TextInput(attrs={'required':'required','class':'form-control','placeholder':'mis.2022'}),
			'tahun_akhir':forms.TextInput(attrs={'required':'required','class':'form-control','placeholder':'mis.2024'}),
			'keterangan':forms.TextInput(attrs={'required':'required','class':'form-control','placeholder':'analisa penyebab naik dan turun'}),
		}

class inputBab3BNKB(forms.ModelForm):
	class Meta:
		model = bab3_bbnkb
		fields = ['bulan_awal','bulan_akhir','tahun_awal','tahun_akhir','keterangan']

		widgets = {
			'bulan_awal': forms.Select(attrs={'class':'form-control'}),
			'bulan_akhir': forms.Select(attrs={'class':'form-control'}),
			'tahun_awal':forms.TextInput(attrs={'required':'required','class':'form-control','placeholder':'mis.2022'}),
			'tahun_akhir':forms.TextInput(attrs={'required':'required','class':'form-control','placeholder':'mis.2024'}),
			'keterangan':forms.TextInput(attrs={'required':'required','class':'form-control','placeholder':'analisa penyebab naik dan turun'}),
		}
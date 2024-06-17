from django import forms
from lhe.models import headerLHE, bab2_tatausaha_kepegawaian_normatif
from surat_tugas.models import TrxSuratTugas
from bootstrap_datepicker_plus.widgets import DatePickerInput

class inputHeaderLHE(forms.ModelForm):
	class Meta:
		model = headerLHE
		fields = ['suratTugas','nomor_lhe','tanggal_lhe']

		widgets = {
			'suratTugas': forms.Select(attrs={'class':'form-control'}),
			'nomor_lhe':forms.TextInput(attrs={'required':'required','class':'form-control'}),
			'tanggal_lhe':DatePickerInput(attrs={'required':'required','class':'form-control','min':'<script></script'})
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
			'nama':forms.TextInput(attrs={'required':'required','class':'form-control'}),
			'nip':forms.TextInput(attrs={'required':'required','class':'form-control'})
		}
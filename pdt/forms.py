from django import forms
from .models import ManagerPhase

class PhaseOpenForm(forms.ModelForm):
	class Meta:
		model = ManagerPhase
		fields = ('sloc','hours', 'defects')
	
	def clean_sloc(self):
		sloc = self.cleaned_data.get('sloc')
		if sloc < 1:
			raise forms.ValidationError("Please Enter a valid SLOC number i.e. at least 1.")
		return sloc
		
	def clean_hours(self):
		hours = self.cleaned_data.get('hours')
		if hours < 1:
			raise forms.ValidationError("Please Enter a valid hours number i.e. at least 1.")
		return hours
		
	def clean_defects(self):
		defects = self.cleaned_data.get('defects')
		if defects < 0:
			raise forms.ValidationError("Please Enter a valid hours number i.e. at least 0.")
		return defects
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Signin


class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']
		widgets = {
			'password': forms.PasswordInput()
		}

	def clean_username(self):
		username = self.cleaned_data.get('username')
		return username

	def clean_password(self):
		password = self.cleaned_data.get('password')
		return password

class RegistrationForm(forms.ModelForm):
	class Meta:
		model = Signin
		fields = ('username','role','password')
		widgets = {
			'password': forms.PasswordInput()
		}

	def clean_username(self):
		username = self.cleaned_data.get('username')
		return username

	def clean_password(self):
		password = self.cleaned_data.get('password')
		return password
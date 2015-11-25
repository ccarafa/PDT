from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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

class RegistrationForm(UserCreationForm):
	role = forms.CharField(required=True)

	class Meta:
		model = User
		fields = ('username','role','password1','password2')

	def save(self,commit=True):
		user = super(RegistrationForm, self).save(commit=False)#save is not commited in super
		user.role=self.cleaned_data['role']
		user.password=self.cleaned_data["password1"];

		if commit:
			user.save()
		return user
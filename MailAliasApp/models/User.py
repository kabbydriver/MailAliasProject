from django.db import models
from django.forms import ModelForm

class User(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)

	def __str__(self):
		return self.first_name + " " + self.last_name

class NewUserForm(ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name']
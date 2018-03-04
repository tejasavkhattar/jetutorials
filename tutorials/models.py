from django.db import models

# Create your models here.

class contact(models.Model):
	email = models.EmailField(max_length=120)
	full_name = models.CharField(max_length=120)
	subject = models.CharField(max_length=200)
	message = models.CharField(max_length=400)  

	def __str__(self):
		return self.email

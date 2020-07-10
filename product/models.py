from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=30, unique=True, null=False, blank=False)
	image = models.TextField(null=True, blank=True)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	description = models.TextField(null=True, blank=True)
	unit = models.CharField(max_length=30, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
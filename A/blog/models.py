from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
	title = models.CharField(max_length=128, null=False, blank=False)

	def __str__(self):
		return self.name

class Product(models.Model):
	category = models.ManyToManyField(Category, related_name='products')
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	image = models.ImageField(null=False, blank=True)
	description = RichTextField()
	s_price = models.IntegerField()
	t_price = models.IntegerField()
	available = models.BooleanField(default=True)

	def __str__(self):
		return self.name
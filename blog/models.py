from django.db import models
from datetime import datetime,date,time
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class Category(models.Model):
	title = models.CharField(max_length=128, null=False, blank=False)

	def __str__(self):
		return self.title

class Product(models.Model):
	name = models.CharField(max_length=200)
	cover = models.FileField(upload_to="ps", null=True, blank=True)
	description = models.TextField(max_length=1200)
	category = models.ForeignKey('Category', on_delete=models.CASCADE)
	s_price = models.IntegerField()
	t_price = models.IntegerField()
	available = models.BooleanField(default=True)

	def __str__(self):
		return self.name


class Message(models.Model):
	name = models.CharField(max_length=120,blank=False,null=False)
	email = models.EmailField(max_length=120,blank=False,null=False)
	subject = models.CharField(max_length=120,blank=False,null=False)
	message_body = models.TextField(max_length=2000,blank=False,null=False)
	create_at =  models.DateTimeField(default=datetime.now)

	def __str__(self):
		return f'{self.name} / {self.subject}'

#Reservation Functions and Model ---------------------------------------------------------------
def allow_day(value):
	today = date.today()
	dw = value.weekday()
	if value < today:
		raise ValidationError('Reservation cannot be in the past.')
	elif dw == 6 or dw == 5 :
		raise ValidationError("you can't reserv on Sunday or Saturday")

def open_hours(value):
	open = time(8,00)
	close = time(20,0)
	if value < open:
		raise ValidationError("Too Early, The Cafe opens at '8:00'")
	elif value > close:
		raise ValidationError("Too Late. Cafe is closes at '22:00'")

def person_limit(value):
	zero_person = 0
	max_person = 5
	if value == zero_person:
		raise ValidationError("Determine the number of people. Can't be zero (0)")
	elif value > max_person : 
		raise ValidationError("More than '5' people are not allowed for booking")

class ReservationInfo(models.Model):
	name = models.CharField(max_length=120,blank=False,null=False)
	phone_regex = RegexValidator(regex="^(\\+98|0)?9\\d{9}$", message="Phone number is not valid in Iran Country")
	phone = models.CharField(validators=[phone_regex],max_length=13,blank=False,null=False)
	r_date = models.DateField(validators=[allow_day])
	r_time = models.TimeField(validators=[open_hours])
	person = models.PositiveIntegerField(validators=[person_limit])
	create_at =  models.DateTimeField(default=datetime.now)
	visit = models.BooleanField(default=False)


	def __str__(self):
		return f'{self.name} / {self.r_date} / {self.r_time} (for {self.person} People)'
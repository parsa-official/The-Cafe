from django import forms
from .models import Message,ReservationInfo
from django.core.exceptions import ValidationError
from datetime import date

class UserMessageForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = ('name', 'email', 'subject', 'message_body')
		labels = {
			'name' : '',
			'email' : '',
			'subject' : '',
			'message_body' : ''
		}
		widgets = {
			'name' : forms.TextInput(attrs={'placeholder': 'Your Name' ,'class' : 'form-control bg-transparent p-4'}),
			'email' : forms.EmailInput(attrs={'placeholder': 'Your Email' ,'class' : 'form-control bg-transparent p-4'}),
			'subject' : forms.TextInput(attrs={'placeholder': 'Subject' ,'class' : 'form-control bg-transparent p-4'}),
			'message_body' : forms.Textarea(attrs={'placeholder': 'Message' ,'class' : 'form-control bg-transparent p-4'}),
		}

class UserReservationForm(forms.ModelForm):
	class Meta:
		model = ReservationInfo
		fields = ('name', 'phone', 'r_date', 'r_time', 'person')
		labels = {
		    'name' : '',
		    'phone' : '',
			'r_date' : '',
			'r_time' : '',
			'person' : ''
		}

		widgets = {
			'name' : forms.TextInput(attrs={'placeholder': 'Name','class' : 'form-control bg-transparent text-white border-primary p-4'}),
			'phone' : forms.TextInput(attrs={'placeholder': 'Phone Number','class' : 'form-control bg-transparent text-white border-primary p-4'}),
			'r_date' : forms.DateInput(attrs={'type' : 'date', 'placeholder': 'Date', 'class' : 'form-control bg-transparent text-white border-primary p-4'}),
			'r_time' : forms.TimeInput(attrs={'type' : 'time', 'placeholder': 'Time', 'class' : 'form-control bg-transparent text-white border-primary p-4'}),
			'person' : forms.NumberInput(attrs={'required':'False','placeholder': 'Person', 'class' : 'form-control bg-transparent text-white border-primary p-4'})
		}

	def clean_phone(self):
			c_phone = self.cleaned_data['phone']
			user_phone = ReservationInfo.objects.filter(phone=c_phone, visit=False).exists()
			if user_phone:
					raise ValidationError('you have active reservation')
			return c_phone

from django.shortcuts import render,redirect
from django.views import View
from .models import Product,Category,Message,ReservationInfo
from .forms import UserMessageForm,UserReservationForm
from django.contrib import messages

class Home(View):
    def get(self, request):
        return render(request, 'blog/home.html')

class Menu(View):
	def get(self, request, *args, **kwargs):
		products = Product.objects.all()
		categories = Category.objects.all()
		return render(request, 'blog/menu.html', {'products':products, 'categories':categories}) 

class Contact(View):
	form_class = UserMessageForm
	template_name = 'blog/contact.html'

	def get(self, request):
		form = self.form_class
		return render(request, self.template_name, {'form':form})
	
	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
				cd = form.cleaned_data
				data = Message.objects.create(name=cd['name'], email=cd['email'], subject=cd['subject'], message_body=cd['message_body'])
				data.save()
				messages.success(request, 'your message submitted successfully', 'success')
				return redirect('blog:contact')
		return render(request, self.template_name, {'form': form})

class Reservation(View):
	form_class = UserReservationForm	
	template_name = 'blog/reservation.html'

	def get(self, request):
		form = self.form_class
		return render(request, self.template_name,{'form' : form})

	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
				cd = form.cleaned_data
				data = ReservationInfo.objects.create(name=cd['name'], phone=cd['phone'], r_date=cd['r_date'], r_time=cd['r_time'], person=cd['person'])
				data.save()
				messages.success(request, 'your reservation submitted successfully', 'success')
				return redirect('blog:reservation')
		return render(request, self.template_name, {'form': form})
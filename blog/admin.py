from django.contrib import admin
from .models import Category,Product,Message,ReservationInfo

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Message)
admin.site.register(ReservationInfo)
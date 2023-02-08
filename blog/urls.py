from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('reservation/', views.Reservation.as_view(), name="reservation"),
]
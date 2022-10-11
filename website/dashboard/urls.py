from django.urls import path
from . import views

# implement your views here

urlpatterns = [

    path('dashboard', views.dashboard, name='dashboard'),

]

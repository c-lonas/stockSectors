from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tech/', views.tech, name='tech'),
    path('finance/', views.fin, name='fin'),
    path('realestate/', views.real, name='real'),
    path('health/', views.health, name='health'),
    path('industry/', views.industry, name='industry'),
    path('crypto/', views.crypto, name='crypto')
]
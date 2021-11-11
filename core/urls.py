from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name= 'about'),
    path('store/', views.store, name= 'store'),
    path('contact/', views.contact, name= 'contact'),
]
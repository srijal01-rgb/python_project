from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_success/', views.order_success, name='order_success'),
]

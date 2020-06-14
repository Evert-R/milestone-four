from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('addcart/<id>', views.add_cart, name='add_cart'),
    path('removecart/<id>', views.remove_cart, name='remove_cart'),
]

from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.all_shop_works, name='all_shop_works'),
    path('<int:pk>', views.shop_details, name='shop_details'),
]

from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.log_in, name='log_in'),
    path('logout/', views.log_out, name='log_out'),
    path('register/', views.register_user, name='register_user'),
    path('userdetails/', views.add_user_details,
         {'next_page': 'shop:all_shop_works'}, name='add_user_details'),
    path('shippingdetails/', views.add_user_details,
         {'next_page': 'checkout:check_out'}, name='shipping_details'),
]
from django.urls import path

from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.check_out, name='check_out'),

]

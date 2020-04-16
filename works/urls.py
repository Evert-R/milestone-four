from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_works, name='works'),
    path('test/', views.all_test, name='test'),
]

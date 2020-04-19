from django.urls import path

from . import views

app_name = 'works'
urlpatterns = [
    path('', views.all_works, name='all_works'),
    path('<int:pk>', views.work_details, name='work_details'),
]

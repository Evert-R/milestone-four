from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('editworks/', views.edit_works, name='add_works'),
    path('editworks/<int:pk>', views.edit_works, name='edit_works'),
]

from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('EditWorksForm/', views.edit_works, name='add_works'),
    path('EditWorksForm/<int:pk>', views.edit_works, name='edit_works'),
]

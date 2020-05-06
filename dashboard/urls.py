from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('addwork/', views.edit_works,
         name='add_works'),
    path('editworks/', views.list_works,
         name='list_works'),
    path('listworks/<filter>', views.list_works,
         name='list_filtered_works'),
    path('worksorder/<int:pk>',
         views.set_works_order, name='set_works_order'),
    path('editworks/<int:pk>', views.edit_works, name='edit_works'),
    path('deletework/<int:pk>',
         views.delete_work, name='delete_work'),
    path('deleteimage/<int:pk>',
         views.delete_image, name='delete_image'),
    path('listorders/<filter>', views.list_orders,
         name='list_orders'),
]

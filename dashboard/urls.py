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
    path('editworks/<int:pk>', views.edit_works,
         name='edit_works'),
    path('worksorder/<int:pk>',
         views.set_works_order, name='set_works_order'),
    path('shoporder/<int:pk>',
         views.set_shop_order, name='set_shop_order'),
    path('imageorder/<int:pk>',
         views.set_image_order, name='set_image_order'),
    path('deletework/<int:pk>',
         views.delete_work, name='delete_work'),
    path('deleteimage/<int:pk>',
         views.delete_image, name='delete_image'),
    path('shopimage/<int:pk>',
         views.set_shop_image, name='set_shop_image'),
    path('unsetshopimage/<int:pk>',
         views.unset_shop_image, name='unset_shop_image'),

    path('editcategories/<int:pk>',
         views.edit_categories, name='edit_categories'),
    path('addcategory/',
         views.edit_categories, name='add_category'),

    path('setshopmessage/',
         views.set_shop_message, name='set_shop_message'),

    path('editworktypes/<int:pk>',
         views.edit_work_types, name='edit_work_types'),
    path('addworktype/',
         views.edit_work_types, name='add_work_type'),

    path('editworksizes/<int:pk>',
         views.edit_work_sizes, name='edit_work_sizes'),
    path('addworksize/',
         views.edit_work_sizes, name='add_work_size'),

    path('editmaterials/<int:pk>',
         views.edit_materials, name='edit_materials'),
    path('addmaterial/',
         views.edit_materials, name='add_material'),


    path('listorders/', views.list_orders,
         name='list_orders'),
    path('vieworder/<int:pk>', views.view_order,
         name='view_order'),
    path('updateorder/<int:pk>/<action>', views.update_order,
         name='update_order'),

    path('settings/', views.edit_settings,
         name='edit_settings'),

    path('editshipping/<int:pk>',
         views.edit_shipping, name='edit_shipping'),
    path('addshipping/',
         views.edit_shipping, name='add_shipping'),

]

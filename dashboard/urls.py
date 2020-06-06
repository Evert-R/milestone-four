from django.urls import path

from .views.views_about import *
from .views.views_shop import *
from .views.views_works import *
from .views.views_attributes import *

app_name = 'dashboard'
urlpatterns = [
    # Edit/add work items
    path('addwork/', edit_works,
         name='add_works'),
    path('editworks/', list_works,
         name='list_works'),
    path('listworks/<filter>', list_works,
         name='list_filtered_works'),
    path('editworks/<int:pk>', edit_works,
         name='edit_works'),
    path('worksorder/<int:pk>',
         set_works_order, name='set_works_order'),
    path('shoporder/<int:pk>',
         set_shop_order, name='set_shop_order'),
    path('imageorder/<int:pk>',
         set_image_order, name='set_image_order'),
    path('deletework/<int:pk>',
         delete_work, name='delete_work'),
    path('deleteimage/<int:pk>',
         delete_image, name='delete_image'),
    path('shopimage/<int:pk>',
         set_shop_image, name='set_shop_image'),
    path('unsetshopimage/<int:pk>',
         unset_shop_image, name='unset_shop_image'),

    # Manage global attributes
    path('addcategory/',
         edit_categories, name='add_category'),
    path('editcategories/<int:pk>',
         edit_categories, name='edit_categories'),

    path('editworktypes/<int:pk>',
         edit_work_types, name='edit_work_types'),
    path('addworktype/',
         edit_work_types, name='add_work_type'),

    path('addworksize/',
         edit_work_sizes, name='add_work_size'),
    path('editworksizes/<int:pk>',
         edit_work_sizes, name='edit_work_sizes'),

    path('addmaterial/',
         edit_materials, name='add_material'),
    path('editmaterials/<int:pk>',
         edit_materials, name='edit_materials'),

    # Global settings
    path('settings/', edit_settings,
         name='edit_settings'),
    path('setshopmessage/',
         set_shop_message, name='set_shop_message'),
    path('addshipping/',
         edit_shipping, name='add_shipping'),
    path('editshipping/<int:pk>',
         edit_shipping, name='edit_shipping'),

    # Order handling
    path('listorders/', list_orders,
         name='list_orders'),
    path('vieworder/<int:pk>', view_order,
         name='view_order'),
    path('updateorder/<int:pk>/<action>', update_order,
         name='update_order'),
]

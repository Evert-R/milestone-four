from django.contrib import admin
from .models import shop_items, work_types, materials, work_sizes, shipping, reviews

# Register your models here.
admin.site.register(shop_items)
admin.site.register(work_types)
admin.site.register(materials)
admin.site.register(work_sizes)
admin.site.register(shipping)
admin.site.register(reviews)

from django.contrib import admin
from .models import work_items, categories, work_types, materials, work_sizes

# Register your models here.
admin.site.register(work_items)
admin.site.register(categories)
admin.site.register(work_types)
admin.site.register(materials)
admin.site.register(work_sizes)

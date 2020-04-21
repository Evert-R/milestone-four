from django.contrib import admin
from .models import work_items, categories

# Register your models here.
admin.site.register(work_items)
admin.site.register(categories)

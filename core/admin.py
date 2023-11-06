from django.contrib import admin
from .models import *

# Register your models here.

class PostInventory(admin.ModelAdmin):
    list_display = ['id_users','id_types','id_brands','serialNumber','lanMac']
    list_display_links = ['id_users']
    list_filter = ['id_users','id_types','id_brands','serialNumber','lanMac']


admin.site.register(users)
admin.site.register(types)
admin.site.register(brands)
admin.site.register(inventory,PostInventory)
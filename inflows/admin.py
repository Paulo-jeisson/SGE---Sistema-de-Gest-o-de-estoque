from django.contrib import admin
from . import models


class InflowAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'product', 'quantity', 'descripton')
    search_fields = ('supplier_name', 'product_title',)


admin.site.register(models.Inflow, InflowAdmin)

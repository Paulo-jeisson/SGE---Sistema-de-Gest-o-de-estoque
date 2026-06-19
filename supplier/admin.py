from django.contrib import admin
from . import models


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'descriptions',)
    search_fields = ('name',)


admin.site.register(models.Supplier, SupplierAdmin)

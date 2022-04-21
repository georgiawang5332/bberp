from django.contrib import admin
from meatOrder.models import *


# Register your models here.
class MeatProductNameAdmin(admin.ModelAdmin):
    list_display = ('no', 'meatID', 'meatName')
    list_display_links = ('meatName', )
    fields = ('meatID', 'meatName')

    list_filter = ('meatName',)
    search_fields = ('no', 'meatID', 'meatName')
    ordering = ('-meatID',)


admin.site.register(MeatProductName, MeatProductNameAdmin)


class SupplierNameAdmin(admin.ModelAdmin):
    list_display = ('no', 'supplier_name')
    list_display_links = ('supplier_name', )
    fields = ('supplier_name',)

    list_filter = ('supplier_name',)
    search_fields = ('no', 'supplier_name')
    ordering = ('-supplier_name',)


admin.site.register(SupplierName, SupplierNameAdmin)


class MeatOrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'product_name', 'quantity', 'unit_price', 'subtotal', 'remark', 'supplier_name', 'procurement_staff')
    list_display_links = ('product_name', )
    fields = ('order_number', 'product_name', 'quantity', 'unit_price', 'subtotal', 'remark', 'supplier_name', 'procurement_staff')

    list_filter = ('product_name',)
    search_fields = ('order_number', 'product_name__meatName', 'supplier_name__supplier_name', 'procurement_staff')
    ordering = ('-unit_price',)
    # form = MultSearchForm


admin.site.register(MeatOrder, MeatOrderAdmin)

from django.contrib import admin

from payment.models import Order, Discount, Tax


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ('item', 'tax', 'discount', )


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    fields = ('discount',)


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    fields = ('tax',)

from django.contrib import admin

from product.models import Item


@admin.register(Item)
class CommentAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'price', 'currency')

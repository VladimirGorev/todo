from django.contrib import admin
from todo_item.models import ItemModel


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'name', 'is_done', 'user']
    list_filter = ['created', 'name', 'is_done', 'user']
    search_fields = ['name', 'user']


admin.site.register(ItemModel, ItemAdmin)
from django.contrib import admin
from todo_item.models import ItemModel


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'name', 'is_done', 'expire_date']
    list_filter = ['created', 'name', 'is_done']
    search_fields = ['name', 'is_done']


admin.site.register(ItemModel, ItemAdmin)
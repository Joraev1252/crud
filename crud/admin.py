from django.contrib import admin
from crud.models import Account


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'surname')
    list_filter = ('id',)


admin.site.register(Account, TodoAdmin)

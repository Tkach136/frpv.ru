from django.contrib import admin
from .models import Bid, Topic, Entry, Info


class EntryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Информация', {'fields': ['header', 'topic', 'text']}),
        ('Вложения', {'fields': ['attachment', 'image']})
    ]
    list_display = ('date', 'changed', 'header', 'topic')
    list_filter = ['date', 'changed', 'topic']
    search_fields = ['header']


class BidAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'INN', 'chief', 'email')
    list_filter = ['date']
    search_fields = ['INN', 'name']


class InfoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Информация', {'fields': ['page', 'blockname', 'header', 'group', 'text', 'price']}),
        ('Вложения', {'fields': ['attachment', 'image']})
    ]
    list_display = ['header', 'page', 'blockname', 'group', ]
    list_filter = ['page', 'group']
    search_fields = ['header']


admin.site.register(Bid, BidAdmin)
admin.site.register(Topic)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Info, InfoAdmin)

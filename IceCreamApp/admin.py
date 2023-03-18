from django.contrib import admin
from .models import Store, Tub
# Register your models here.
# @admin.action(description = 'Mark selected post as published')
# def make_published(modeladmin, request, queryset):
#     queryset.update(tag = 'p')
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'contact_email']
    ordering = ['name']
    
class TubAdmin(admin.ModelAdmin):
    list_display = ['flavour', 'size', 'store']
    ordering = ['flavour']


admin.site.register(Store, StoreAdmin)
admin.site.register(Tub, TubAdmin)
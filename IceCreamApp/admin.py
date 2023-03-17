from django.contrib import admin
from .models import Store, Tub
# Register your models here.
# @admin.action(description = 'Mark selected post as published')
# def make_published(modeladmin, request, queryset):
#     queryset.update(tag = 'p')
    
class TubAdmin(admin.ModelAdmin):
    list_display = ['flavour', 'size', 'store']
    ordering = ['ID']
    #actions = [make_published]

admin.site.register(Store)
admin.site.register(Tub)
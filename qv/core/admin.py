from django.contrib import admin
from core.models import Dataset

class DatasetAdmin(admin.ModelAdmin):
    #fields display on change list
    list_display = ['name','created']
    #fields to filter the change list with
    list_filter = ['created']
    #fields to search in change list
    search_fields = ['name','file_field__name']
    #enable the date drill down on change list
    date_hierarchy = 'created'
    save_on_top = True

admin.site.register(Dataset,DatasetAdmin)

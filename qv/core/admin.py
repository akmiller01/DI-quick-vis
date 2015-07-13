from django.contrib import admin
from core.models import Data

class DataAdmin(admin.ModelAdmin):
    save_on_top = True

admin.site.register(Data,DataAdmin)

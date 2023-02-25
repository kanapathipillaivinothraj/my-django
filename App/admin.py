from django.contrib import admin

# Register your models here.
from App.models import detail_dataBase


class admindata(admin.ModelAdmin):
    list_display = ['Name' ,'id']


admin.site.register(detail_dataBase,admindata)

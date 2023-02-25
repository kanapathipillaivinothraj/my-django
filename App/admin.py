from django.contrib import admin

# Register your models here.
from App.models import detail_dataBase  


class controaler_data(admin.ModelAdmin):
    details = ['No','Name','Address','Image','Links','Salary']

admin.site.register(detail_dataBase,controaler_data)
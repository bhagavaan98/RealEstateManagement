from django.contrib import admin
from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register([Unit,Tenant,Lease])

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display=["name","address","location","features"]   

    

# admin:bhagavaan
# password:1234

#eshwar =normal user
#6789
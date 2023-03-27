from django.contrib import admin
from .models import Vehicle,User,Vehicle_Types
# Register your models here.


admin.site.register(User)

@admin.register(Vehicle_Types)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id','number','type','model','decription')
from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.


# CarModelInline class
class CarModelInLine(admin.StackedInline):
    model = CarModel
    extra = 5

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ["name","dealer_id","type","year"]
    list_filter = ["year"]
    search_fields = ["name"]
    

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInLine]
    list_display = ["name","description"]
    search_fields = ["name"]
    
# Register models here
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)

from django.contrib import admin
from cars.models import Car, Brand

#admin para o modelo Car
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value') #mostra os campos que serão exibidos na lista de carros no admin
    search_fields = ('model','brand',) #permite buscar pelo modelo do carro no admin  
    
#admin para o modelo Brand
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Car, CarAdmin) #registra o modelo Car no admin
admin.site.register(Brand, BrandAdmin) #registra o modelo Brand no admin    


    
    
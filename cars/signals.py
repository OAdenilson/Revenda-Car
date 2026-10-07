from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver  # recebe o sinal e executa a funcao 
from cars.models import Car, CarInventory
    
def car_inventory_update():                  #Função para atualizar o inventário
    cars_count = Car.objects.all().count()   #quantidade de carros no inventário
    cars_value = Car.objects.aggregate(
        total_value=Sum('value'))['total_value']   #Valor total dos carros no inventário
    CarInventory.objects.create(                   #Cria um novo inventário com a quantidade e valor dos carros
        cars_count=cars_count,                    #Quantidade de carros no inventário
        cars_value=cars_value                     #Valor total dos carros no inventário
    )
    
@receiver(pre_save, sender=Car)     # pre_save: sinal que sera executado antes de salvar o objeto/Carro
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:   #Se a biografia for diferente de None    
        instance.bio = 'Bio gerada automaticamente !' #Se a biografia for None, define uma biografia padrão

    
@receiver(post_save, sender=Car)     # post_save: sinal que sera executado apos salvar o objeto/Carro
def car_post_save(sender, instance, **kwargs):   
    car_inventory_update()            #Atualiza o inventário
    
    
@receiver(post_delete, sender=Car)     # post_delete: sinal que sera executado apos deletar o objeto/Carro
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()            #Atualiza o inventário
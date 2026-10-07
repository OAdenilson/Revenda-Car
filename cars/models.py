from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name      #retorna o nome da marca quando o objeto é exibido como string
    
           

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') #related_name='car_brand' é o nome do relacionamento entre o carro e a marca
    factory_year = models.IntegerField(blank=True, null=True)    #blank=True, null=True significa que o campo pode ser vazio ou nulo
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True) #upload_to='cars/' é o diretório onde as fotos serão salvas
    bio = models.TextField(blank=True, null=True) #bio é o campo de biografia do carro
    
    
    
    def __str__(self):
        return self.model      #retorna o modelo do carro quando o objeto é exibido como string
    

class CarInventory(models.Model):       #modelo para o inventário de carros
    cars_count = models.IntegerField()  #quantidade de carros no inventário
    cars_value = models.FloatField()     #valor total dos carros no inventário
    created_at = models.DateTimeField(auto_now_add=True)   #data e hora de criação do inventário
    
    class Meta:
        ordering = ['-created_at']       #ordena o inventário pela data de criação em ordem decrescente
    
    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'  #retorna a Quantidade e o Valor total dos carros no inventário quando o objeto é exibido como string
from django import forms
from cars.models import Car

    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car                 # o form usa o Model car "o bancos de dados ja existente"
        fields = '__all__'          # todos os campos existente no Model entram automaticamente no formulario 
        
        
    def clean_value(self):         # clean é a sintaxe obrigatoria a escrever quando quer ser criar uma validacao / aqui clean_value feita validacao sobre valor do carro
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor minimo do carro deve ser de R$15.000')  # adiciona mensagem de erro para usuario  
        return value    
    
    
         
    def clean_factory_year(self):  
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Impossivel cadastrar veiculos com ano abaixo de 1975')
        return factory_year
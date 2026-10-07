from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator 
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
    
class CarsListView(ListView):        # Classe para listar todos os carros em estoque
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    
    def get_queryset(self):          # filtar os carros por nome 
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars 
    
    
    
class CarDetailView(DetailView):              # detalha 1 unico Objeto/carro no projeto....renderiza o carro sozinho na tela 
    model = Car
    template_name = 'car_detail.html'    
    
                   
                  
@method_decorator(login_required(login_url='login'), name='dispatch')      # decorador para verificar se o usuario esta logado
class NewCarCreateView(CreateView):                                       # classe para criar um carro novo/ com metodos GET e Post 
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars'
    

    
@method_decorator(login_required(login_url='login'), name='dispatch')      # decorador para verificar se o usuario esta logado
class CarUpdateView(UpdateView):                                           # Atualiza o objeto/carro ja existente no sistema
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
        
    def get_success_url(self):             # Funcao para redirecionar o usuario apos clicar no botao salvar atualizacoes 
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})
    
    
@method_decorator(login_required(login_url='login'), name='dispatch')      # decorador para verificar se o usuario esta logado
class CarDeleteView(DeleteView):                                           # Deleta o objeto/carro do sistema 
    model = Car    
    template_name = 'car_delete.html'
    success_url = '/cars/'
        
    
    
    
    
        
    

  
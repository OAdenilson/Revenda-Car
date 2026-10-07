from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  #formulario pronto ja do django para crir form de cadastrar usuario
from django.contrib.auth import authenticate, login, logout   #funcao pronta do django para autenticacao e validacao de usuario.
from django.shortcuts import render, redirect


def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form' : user_form})




def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm()
    else:                   
        login_form = AuthenticationForm()      #AuthenticationForm é um formulario ja pronto do django so precisa importar ele .
    return render (request, 'login.html', {'login_form' : login_form})


def logout_view(request):
    logout(request)
    return redirect('cars_list')
    
    
    
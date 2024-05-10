from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register_view(request):
    if request.method == "POST": # se a requisiçao for post
        user_form = UserCreationForm(request.POST) # carrega o formulario com os dados
        if user_form.is_valid(): # verifica se o formulario eh valido
            user_form.save() # salva
            return redirect('cars_list') # redireciona para login
    else:
        user_form = UserCreationForm() # formulario pronto do django
    return render(request, 'register.html', {'user_form': user_form})

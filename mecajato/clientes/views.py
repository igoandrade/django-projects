from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente, Carro

# Create your views here.
def clientes(request):
    if request.method == "GET":
        return render(request, "clientes.html", context=None)
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        
        modelos = request.POST.getlist('modelo')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')

        carros = list(zip(modelos, placas, anos))

        cliente = Cliente.objects.filter(cpf=cpf)
        if cliente.exists():
            context = {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'carros': carros}
            return render(request, "clientes.html", context)

        cliente = Cliente(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf
        )
        cliente.save()


        for modelo, placa, ano in carros:
            carro = Carro(
                modelo=modelo,
                placa=placa,
                ano=ano,
                cliente=cliente
            )
            carro.save()
        
        return render(request, "clientes.html", context=None)



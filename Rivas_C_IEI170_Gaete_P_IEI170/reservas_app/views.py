from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from reservas_app.models import Reserva
from reservas_app.forms import FormReserva

# Render 
def index(request):
    return render(request, 'index.html')

def listadoReserva(request):
    reservas = Reserva.objects.all()
    data = {'reservas': reservas}
    return render(request, 'listar_reservas.html', data)

def agregarReserva(request):
    form = FormReserva()
    if request.method == 'POST':
        form = FormReserva(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_re')
    data = {'form': form}
    return render(request, 'agregar_reservas.html', data)

def eliminarReserva(request, id):
    reservas = Reserva.objects.get(id = id)
    reservas.delete()
    return redirect('listar_re')

def modificarReserva(request, id):
    reserva = Reserva.objects.get(id = id)
    form = FormReserva(instance=reserva)

    if request.method == 'POST':
        form = FormReserva(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('listar_re'))
  
    data = {'form': form}
    return render (request, 'agregar_reservas.html', data)
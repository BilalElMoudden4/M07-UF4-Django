from django.shortcuts import render, redirect
from .models import Usuari, Rol
from .forms import UsuariForm

def index(request):
    usuaris = Usuari.objects.all()
    return render(request, 'index.html', {'usuaris': usuaris})

def create(request):
    form = UsuariForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'create.html', {'form': form})

def update(request, id):
    usuari = Usuari.objects.get(id=id)
    form = UsuariForm(request.POST or None, instance=usuari)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'update.html', {'form': form})

def delete(request, id):
    usuari = Usuari.objects.get(id=id)
    if request.method == 'POST':
        usuari.delete()
        return redirect('index')
    return render(request, 'delete.html', {'usuari': usuari})

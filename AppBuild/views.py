from django.shortcuts import render, redirect
from django.views.generic import ListView
from AppBuild.forms import*
from AppBuild.models import *


def busqueda_tipo_post(request):
    tipo = request.GET.get('tipo')

    obras = Obra.objects.filter(tipo__icontains= tipo)
    contexto = {
       'obras': obras
    }

    return render(request, 'AppBuild/tipo_filtrado.html', contexto)

def busqueda_tipo(request):
    contexto = {
        'form': BusquedaObraFormulario(),
    }

    return render(request, 'AppBuild/busqueda_tipo.html', contexto)
def arquitecto_formulario(request):

    if request.method == 'POST':
        mi_formulario = ArquitectoFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            arquitecto1 = Arquitecto(nombre=data.get('nombre'), apellido=data.get('apellido'), edad=data.get('edad'), matricula=data.get('matricula'))
            arquitecto1.save()

            return redirect('AppBuildArquitectoFormulario')

    contexto = {
        'form': ArquitectoFormulario()
    }

    return render(request, 'AppBuild/arquitecto_formulario.html', contexto)





def obrero_formulario(request):

    if request.method == 'POST':
        mi_formulario = ObreroFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            obrero1 = Obrero(nombre=data.get('nombre'), apellido=data.get('apellido'), edad=data.get('edad'))
            obrero1.save()

            return redirect('AppBuildObreroFormulario')

    contexto = {
        'form': ObreroFormulario()
    }

    return render(request, 'AppBuild/obrero_formulario.html', contexto)






def obra_formulario(request):

    if request.method == 'POST':
        mi_formulario = ObraFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            obra1 = Obra(tipo=data.get('tipo'), inicio=data.get('inicio'))
            obra1.save()

            return redirect('AppBuildObraFormulario')

    contexto = {
        'form': ObraFormulario()
    }

    return render(request, 'AppBuild/obra_formulario.html', contexto)

def inicio(request):
    contexto = {
        "valor1": "este es un valor"
    }
    return render(request, 'index.html', contexto)


class ObraList(ListView):
    model = Obra


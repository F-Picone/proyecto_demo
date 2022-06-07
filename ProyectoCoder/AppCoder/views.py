from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
from django.template import loader

def curso(self):
    curso = Curso(nombre ='desarrollo web', camada = 1238)
    curso.save()
    documento = f'Curso : {curso.nombre}  - Camada {curso.camada}'
    return HttpResponse(documento)

def profesores(request):
    return render(request, 'appCoder/profesores.html')

def estudiantes(request):
    return render(request, 'appCoder/estudiantes.html')

def entregables(self):
    documento = f'Pagina de entregables'
    return HttpResponse(documento)

def cursos(self):
    documento = f'Pagina de cursos'
    return HttpResponse(documento)

def inicio(self):
    plantilla = loader.get_template('AppCoder/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

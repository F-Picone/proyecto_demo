from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
from django.template import loader

def curso(self):
    curso = Curso(nombre ='desarrollo web', camada = 1238)
    curso.save()
    documento = f'Curso : {curso.nombre}  - Camada {curso.camada}'
    return HttpResponse(documento)

def profesores(self):
    documento = f'Pagina de profesores'
    return HttpResponse(documento)

def estudiantes(self):
    documento = f'Pagina de estudiantes'
    return HttpResponse(documento)

def entregables(self):
    documento = f'Pagina de entregables'
    return HttpResponse(documento)

def cursos(self):
    documento = f'Pagina de cursos'
    return HttpResponse(documento)

def inicio(self):
    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

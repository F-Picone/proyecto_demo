from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
from django.template import loader

def curso(self):
    curso = Curso(nombre ='desarrollo web', camada = 1238)
    curso.save()
    documento = f'Curso : {curso.nombre}  - Camada {curso.camada}'
    return HttpResponse(documento)

def mi_plantilla(self):
    plantilla = loader.get_template('plantilla.html')
    documento = plantilla.render()
    return HttpResponse(documento)
    
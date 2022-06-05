from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

def curso(self):
    curso = Curso(nombre ='desarrollo web', camada = 1238)
    curso.save()
    documento = f'Curso : {curso.nombre}  - Camada {curso.camada}'
    return HttpResponse(documento)


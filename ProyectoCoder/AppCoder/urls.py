from django.urls import path
from AppCoder.views import curso,inicio,cursos,entregables,estudiantes,profesores,cursoFormulario


urlpatterns = [
    path('curso/', curso),
    path('profesores/',profesores, name= 'Profesores'),
    path('estudiantes/',estudiantes, name= 'Estudiantes'),
    path('entregables/',entregables, name= 'Entregables'),
    path('cursos/',cursos, name= 'Cursos'),
    path('', inicio, name= 'Inicio'),
    path('cursoFormulario/', cursoFormulario, name= 'cursoFormulario'),
]

from django.urls import path
from AppCoder.views import curso,inicio,cursos,entregables,estudiantes,profesores


urlpatterns = [
    path('curso/', curso),
    path('profesores/',profesores),
    path('estudiantes/',estudiantes),
    path('entregables/',entregables),
    path('cursos/',cursos),
    path('', inicio),
]

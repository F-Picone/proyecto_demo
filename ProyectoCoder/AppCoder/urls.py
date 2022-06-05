from django.urls import path
from AppCoder.views import curso
from AppCoder.views import mi_plantilla

urlpatterns = [
    path('curso/', curso),
    path('plantilla/', mi_plantilla),
]

from django.urls import path
from .views import historia_clinica_por_documento, crear_historia_clinica

urlpatterns = [
    path('historia_clinica/', historia_clinica_por_documento, name='historia_clinica_por_documento'),
    path('crear_historia_clinica/', crear_historia_clinica.as_view(), name='crear_historia_clinica'),
]

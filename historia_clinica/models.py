from django.db import models

class HistoriaClinica(models.Model):
    documento_paciente = models.CharField(max_length=20)
    documento_doctor = models.CharField(max_length=20)
    descripcion = models.TextField()
    enfermedad = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

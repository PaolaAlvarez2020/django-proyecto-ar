from django.db import models


class Enfermedad(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.CharField(max_length=1000, null=True, blank=True)
    estado = models.BooleanField(default=True)
    paciente = models.ForeignKey(
        'pacientes.Paciente', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

from django.db import models

class Sede(models.Model):
    nombre = models.CharField(max_length=255, unique = True)
    
    def __str__(self) -> str:
        return self.nombre
    
class Paciente(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.nombre
    
class Doctor(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.nombre
    
class ObraSocial(models.Model):
    nombre = models.CharField(max_length=255)
    ubicacion = models.ForeignKey(Sede, on_delete=models.SET_NULL, null=True, blank=True)
    director = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    paciente = models.ManyToManyField(Paciente)

from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):          
        return self.name

class Reserva_vuelos(models.Model):
    nombre = models.CharField(max_length=100)
    clase_vuelo = models.TextField(blank=True)
    datos_pasajero = models.TextField(blank=True)
    horarios = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):          
        return self.nombre

    
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Reserva(models.Model):
    nombre = models.CharField(null=False, max_length=80)
    telefono = models.CharField(null=False, max_length=15)
    fecha_reserva = models.CharField(null=False, max_length=15)
    hora = models.CharField(null=False, max_length=15)
    cantidad_personas = models.IntegerField(
        validators=[
            MinValueValidator(1, message='La cantidad de personas debe ser al menos 1.'),
            MaxValueValidator(15, message='La cantidad de personas no puede ser más de 15.')
        ]
    )
    email = models.CharField(null=False, max_length=50)

    # Estados posibles de la reserva
    ESTADOS = (
        ('RESERVADO', 'RESERVADO'),
        ('COMPLETADA', 'COMPLETADA'),
        ('ANULADA', 'ANULADA'),
        ('NO ASISTEN', 'NO ASISTEN'),
    )

    estado = models.CharField(max_length=15, choices=ESTADOS, default='SIN ESTADO', null=False,)
    observacion = models.CharField(null=True, max_length=50)
    

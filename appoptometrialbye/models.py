from django.db import models
from django.urls import reverse
import datatime
from django.core.validators import RegexValidator
# Clase paciente
class Pacientes(models.Model):
    #Campos tabla
    run = models.CharField(primary_key= True, max_length= 9, help_text="Sin puntos ni guion")
    nombre = models.CharField(max_length= 100)
    apellido = models.CharField(max_length= 100)
    genero = models.CharField(max_length= 2, choices= genero_opciones)
    celular_regex = RegexValidator(regex=r'^\+?569?\d{8}$', message = "Número debe ser ingresado en formato '+549XXXXXXXX'.")
    celular = models.CharField("Número de teléfono celular", validators=[celular_regex], max_length = 12, unique = True)
    historial = models.TextField('Historial' blank=True)
    #Metadata
    class Meta:
        ordening = ['apellido']

    #Metodos
    def get_absolute_url(self):
        
        return reverse ('model-detail-view', args=[str(self.id)])
    def __str__(self):
        nombre_apellido = f'{self.nombre} {self.apellido}'
        return nombre_apellido

class Turnos(models.Model):
    fecha = models.DateField()
    dia = models.DateField(default= date.today)
    hora = models.TimeField(default= timezone.now)
    medico = models.CharField(max_length=255, blank=True)
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    motivo = models.CharField('Motivo', max_length=255, blank=True)

    class Meta:
        ordening = ['fecha']

    def __str__(self):
        return "{}".format(self.fecha)
    
       
class Pedidos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=100, choices='descripcion_opciones')
    precio = models.FloatField()
    subtotal = models.FloatField()
    pago = 
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    

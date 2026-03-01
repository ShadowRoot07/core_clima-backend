from django.db import models

class Location(models.Model):
    nombre = models.CharField(max_length=100, help_text="Ej: Huerto Norte o Invernadero")
    latitud = models.FloatField()
    longitud = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.latitud}, {self.longitud})"

class WeatherHistory(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='history')
    temperatura = models.FloatField() # Almacenaremos en Celsius
    humedad = models.FloatField()    # Porcentaje 0-100
    presion = models.FloatField(null=True, blank=True) # hPa
    descripcion = models.CharField(max_length=255) # Ej: "broken clouds"
    icono = models.CharField(max_length=20, null=True, blank=True) # Código de icono de la API
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Weather Histories"
        ordering = ['-fecha_registro'] # El más nuevo primero para las gráficas

    def __str__(self):
        return f"{self.location.nombre} - {self.temperatura}°C a las {self.fecha_registro.strftime('%H:%M')}"


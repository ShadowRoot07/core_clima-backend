from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100, help_text="e.g.: North Garden or Greenhouse")
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.latitude}, {self.longitude})"

class WeatherHistory(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='history')
    temperature = models.FloatField() # Stored in Celsius
    humidity = models.FloatField()    # Percentage 0-100
    pressure = models.FloatField(null=True, blank=True) # hPa
    description = models.CharField(max_length=255) # e.g.: "broken clouds"
    icon = models.CharField(max_length=20, null=True, blank=True) # API Icon code
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Weather Histories"
        ordering = ['-recorded_at']

    def __str__(self):
        return f"{self.location.name} - {self.temperature}°C at {self.recorded_at.strftime('%H:%M')}"


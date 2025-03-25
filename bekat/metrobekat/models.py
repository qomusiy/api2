from django.db import models

# Create your models here.

class MetroBekat(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()
    is_presetable = models.BooleanField(default=False)

    def __str__(self):
        return self.name
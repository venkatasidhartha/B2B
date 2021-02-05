from django.db import models

# Create your models here.
class Food_items(models.Model):
    Food = models.CharField(max_length=100)
    Price = models.FloatField()

    def __str__(self):
        return self.Food
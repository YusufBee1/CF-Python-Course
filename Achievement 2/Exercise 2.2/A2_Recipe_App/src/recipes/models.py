from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=255)
    cooking_time = models.IntegerField(help_text="In minutes")
    difficulty = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name
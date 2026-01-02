from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=255)
    cooking_time = models.IntegerField(help_text="In minutes")
    difficulty = models.CharField(max_length=20, blank=True)
    description = models.TextField()

    def calculate_difficulty(self):
        ingredients_len = len(self.ingredients.split(', '))
        if self.cooking_time < 10 and ingredients_len < 4:
            difficulty = "Easy"
        elif self.cooking_time < 10 and ingredients_len >= 4:
            difficulty = "Medium"
        elif self.cooking_time >= 10 and ingredients_len < 4:
            difficulty = "Intermediate"
        elif self.cooking_time >= 10 and ingredients_len >= 4:
            difficulty = "Hard"
        return difficulty

    def save(self, *args, **kwargs):
        self.difficulty = self.calculate_difficulty()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):
    def setUp(self):
        Recipe.objects.create(name="Tea", ingredients="Water, Tea Leaves", cooking_time=5, difficulty="Easy", description="Hot tea")

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.name, 'Tea')

    def test_cooking_time(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.cooking_time, 5)
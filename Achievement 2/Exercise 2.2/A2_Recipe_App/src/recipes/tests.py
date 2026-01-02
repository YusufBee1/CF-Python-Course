from django.test import TestCase
from django.urls import reverse
from .models import Recipe

class RecipeTests(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(name="Tea", ingredients="Water, Tea", cooking_time=5, description="Hot")

    def test_list_view(self):
        response = self.client.get(reverse('recipes:list'))
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        response = self.client.get(reverse('recipes:detail', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
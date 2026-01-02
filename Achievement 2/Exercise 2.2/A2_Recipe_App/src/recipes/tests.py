from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Recipe
from .forms import RecipesSearchForm

class RecipeTests(TestCase):
    def setUp(self):
        # Create a test user (needed for @login_required pages)
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create a test recipe
        self.recipe = Recipe.objects.create(
            name="Tea", 
            ingredients="Water, Tea", 
            cooking_time=5, 
            description="Hot"
        )

    def test_list_view(self):
        # Log in first
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('recipes:list'))
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        # Log in first
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('recipes:detail', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)

class RecipeFormTest(TestCase):
    def test_form_valid_data(self):
        form = RecipesSearchForm(data={'recipe_name': 'Tea', 'chart_type': '#1'})
        self.assertTrue(form.is_valid())

    def test_form_empty_data(self):
        # Search fields are optional, so empty should still be valid
        form = RecipesSearchForm(data={})
        self.assertTrue(form.is_valid())
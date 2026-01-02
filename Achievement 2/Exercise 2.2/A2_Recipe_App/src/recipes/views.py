from django.shortcuts import render, get_object_or_404
from .models import Recipe

def home(request):
   return render(request, 'recipes/recipes_home.html')

def recipes_list(request):
   recipes = Recipe.objects.all()
   return render(request, 'recipes/recipes_list.html', {'recipes': recipes})

def recipes_detail(request, pk):
   recipe = get_object_or_404(Recipe, pk=pk)
   # FIX: Split the ingredients here in Python
   # This assumes ingredients are separated by commas (e.g., "Flour, Water, Salt")
   ingredients_list = recipe.ingredients.split(',')
   return render(request, 'recipes/recipes_detail.html', {
       'recipe': recipe,
       'ingredients_list': ingredients_list
   })
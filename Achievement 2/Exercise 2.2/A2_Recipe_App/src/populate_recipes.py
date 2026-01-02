import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_project.settings')
django.setup()

from recipes.models import Recipe

recipes_data = [
    {"name": "Lemonade", "ingredients": "Water, Lemon, Sugar", "cooking_time": 5, "description": "Refreshing summer drink."},
    {"name": "Grilled Cheese", "ingredients": "Bread, Cheese, Butter", "cooking_time": 10, "description": "Classic comfort food."},
    {"name": "Omelette", "ingredients": "Eggs, Salt, Pepper, Cheese", "cooking_time": 8, "description": "Quick breakfast."},
    {"name": "Salad", "ingredients": "Lettuce, Tomato, Cucumber, Dressing", "cooking_time": 5, "description": "Healthy side dish."},
    {"name": "Spaghetti Carbonara", "ingredients": "Pasta, Eggs, Cheese, Bacon, Pepper", "cooking_time": 20, "description": "Roman classic."},
    {"name": "Pancakes", "ingredients": "Flour, Milk, Eggs, Sugar, Baking Powder", "cooking_time": 15, "description": "Fluffy breakfast stack."},
    {"name": "Chicken Curry", "ingredients": "Chicken, Curry Powder, Coconut Milk, Onion", "cooking_time": 30, "description": "Spicy and creamy."},
    {"name": "Tomato Soup", "ingredients": "Tomatoes, Onion, Garlic, Cream", "cooking_time": 25, "description": "Perfect for winter."},
    {"name": "Beef Tacos", "ingredients": "Beef, Taco Shells, Lettuce, Cheese, Salsa", "cooking_time": 20, "description": "Tuesday favorite."},
    {"name": "Chocolate Cake", "ingredients": "Flour, Sugar, Cocoa, Eggs, Butter", "cooking_time": 60, "description": "Decadent dessert."},
    {"name": "Guacamole", "ingredients": "Avocado, Onion, Lime, Cilantro", "cooking_time": 10, "description": "Best dip ever."},
    {"name": "French Toast", "ingredients": "Bread, Eggs, Milk, Cinnamon", "cooking_time": 12, "description": "Sweet breakfast."},
    {"name": "Fried Rice", "ingredients": "Rice, Eggs, Peas, Carrots, Soy Sauce", "cooking_time": 15, "description": "Leftover magic."},
    {"name": "Smoothie", "ingredients": "Banana, Berries, Yogurt, Honey", "cooking_time": 5, "description": "Vitamin boost."},
    {"name": "Bruschetta", "ingredients": "Bread, Tomato, Basil, Garlic, Olive Oil", "cooking_time": 10, "description": "Italian appetizer."}
]

for data in recipes_data:
    if not Recipe.objects.filter(name=data['name']).exists():
        r = Recipe(**data)
        r.save() # Automatic difficulty calculation happens here
        print(f"Added: {r.name}")
    else:
        print(f"Skipped (Exists): {data['name']}")

print("Done! 15 Recipes checked/added.")
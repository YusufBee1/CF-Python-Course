# Initialize empty lists
recipes_list = []
ingredients_list = []

def take_recipe():
    # input() always returns a string
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    
    # The "Split" Trap: User enters comma-separated string, we convert to list
    ingredients_input = input("Enter ingredients (separated by a comma and space): ")
    ingredients = ingredients_input.split(", ")
    
    # Create the dictionary
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    
    return recipe

# Main Section
# Ask user how many recipes they want to enter
n = int(input("How many recipes would you like to enter? "))

# Loop n times
for i in range(n):
    # Run the function and get the recipe dictionary
    recipe = take_recipe()
    
    # Check for new ingredients
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
            
    # Add the recipe to the main list
    recipes_list.append(recipe)

# Processing and Output Section
print("\n" + "="*40) # Cosmetic separator

for recipe in recipes_list:
    # Logic Matrix for Difficulty
    cooking_time = recipe['cooking_time']
    num_ingredients = len(recipe['ingredients'])
    difficulty = ""

    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    elif cooking_time >= 10 and num_ingredients >= 4:
        difficulty = "Hard"

    # Print Recipe (Matches Image 4 format)
    print(f"Recipe: {recipe['name']}")
    print(f"Cooking Time (min): {cooking_time}")
    print("Ingredients:")
    for item in recipe['ingredients']:
        print(item)
    print(f"Difficulty level: {difficulty}")
    print("-" * 20) # Divider between recipes

# Final Ingredient List (Matches Image 3 format)
print("\nIngredients Available Across All Recipes")
print("-" * 40)
ingredients_list.sort() # Sort alphabetically
for ingredient in ingredients_list:
    print(ingredient)
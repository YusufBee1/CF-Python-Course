import pickle

def calc_difficulty(cooking_time, ingredients):
    """
    Calculates difficulty based on cooking time and number of ingredients.
    Returns: Easy, Medium, Intermediate, or Hard
    """
    num_ingredients = len(ingredients)
    
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    elif cooking_time >= 10 and num_ingredients >= 4:
        return "Hard"

def take_recipe():
    """
    Takes user input for a recipe and returns a dictionary.
    """
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients_input = input("Enter ingredients (separated by a comma and space): ")
    ingredients = ingredients_input.split(", ")
    
    # Calculate difficulty using the helper function
    difficulty = calc_difficulty(cooking_time, ingredients)
    
    return {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
        'difficulty': difficulty
    }

# --- Main Code ---

filename = input("Enter the filename for your recipe data (e.g., recipes.bin): ")
data = {}
recipes_list = []
all_ingredients = []

try:
    # Try to open the existing file
    file = open(filename, 'rb')
    data = pickle.load(file)
    print("File loaded successfully!")
except FileNotFoundError:
    # If file doesn't exist, initialize empty data
    print("File not found. Creating a new database.")
    data = {'recipes_list': [], 'all_ingredients': []}
except Exception as e:
    # Handle other unexpected errors
    print(f"An error occurred: {e}")
    data = {'recipes_list': [], 'all_ingredients': []}
else:
    # Close the file stream if opened successfully
    file.close()
finally:
    # Extract lists from the dictionary (or empty lists if new)
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']

# User Interaction Loop
n = int(input("How many recipes would you like to enter? "))

for i in range(n):
    recipe = take_recipe()
    
    # Update unique ingredients list
    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)
    
    recipes_list.append(recipe)
    print("Recipe added!")

# Save Data
data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}

try:
    file = open(filename, 'wb')
    pickle.dump(data, file)
    print("Data successfully saved.")
    file.close()
except Exception as e:
    print(f"Error saving file: {e}")
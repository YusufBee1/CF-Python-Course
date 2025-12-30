import pickle

def display_recipe(recipe):
    """
    Displays the details of a single recipe.
    """
    print("")
    print(f"Recipe: {recipe['name']}")
    print(f"Cooking Time (min): {recipe['cooking_time']}")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Difficulty: {recipe['difficulty']}")
    print("-" * 20)

def search_ingredient(data):
    """
    Lists all ingredients, asks user to pick one, and displays recipes containing it.
    """
    all_ingredients = data['all_ingredients']
    
    # 1. Show all available ingredients with numbers
    print("\nAvailable Ingredients:")
    for index, ingredient in enumerate(all_ingredients):
        print(f"{index}: {ingredient}")
    
    try:
        # 2. User picks a number
        n = int(input("\nEnter the number of the ingredient you want to search for: "))
        
        # Access the ingredient from the list using the index
        ingredient_searched = all_ingredients[n]
        print(f"\nSearching for recipes with '{ingredient_searched}'...")
    
    except ValueError:
        print("Error: Please enter a valid number.")
    except IndexError:
        print(f"Error: Number must be between 0 and {len(all_ingredients) - 1}.")
    
    else:
        # 3. Find and display matching recipes
        found_count = 0
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['ingredients']:
                display_recipe(recipe)
                found_count += 1
        
        if found_count == 0:
            print("No recipes found with that ingredient.")


# --- Main Code ---

filename = input("Enter the filename containing your recipe data: ")

try:
    file = open(filename, 'rb')
    data = pickle.load(file)
except FileNotFoundError:
    print("File not found. Please check the name and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    # If file loaded successfully, run the search
    search_ingredient(data)
    file.close()
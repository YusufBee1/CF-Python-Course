class Recipe:
    # Class variable to track ingredients across ALL recipes
    all_ingredients = []

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = None

    # --- Getters and Setters ---
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    # --- Ingredient Handling ---
    def add_ingredients(self, *args):
        # *args allows us to pass a variable number of ingredients
        self.ingredients = list(args)
        self.update_all_ingredients()

    def get_ingredients(self):
        return self.ingredients

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)

    # --- Difficulty Logic ---
    def calculate_difficulty(self):
        # Determine difficulty based on cooking time and ingredient count
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and len(self.ingredients) >= 4:
            self.difficulty = "Hard"

    def get_difficulty(self):
        if not self.difficulty:
            self.calculate_difficulty()
        return self.difficulty

    # --- Search & Display ---
    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    def __str__(self):
        # Returns a string representation of the object
        return f"\nRecipe: {self.name}\nCooking Time: {self.cooking_time} mins\nIngredients: {', '.join(self.ingredients)}\nDifficulty: {self.get_difficulty()}"


def recipe_search(data, search_term):
    print(f"\n--- Searching for recipes with: {search_term} ---")
    found = False
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe) # This triggers the __str__ method
            found = True
    if not found:
        print("No recipes found.")


# --- Main Code ---

# 1. Create Tea
tea = Recipe("Tea")
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.set_cooking_time(5)
print(tea)

# 2. Create Coffee
coffee = Recipe("Coffee")
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
coffee.set_cooking_time(5)
print(coffee)

# 3. Create Cake
cake = Recipe("Cake")
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
cake.set_cooking_time(50)
print(cake)

# 4. Create Banana Smoothie
banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
banana_smoothie.set_cooking_time(5)
print(banana_smoothie)

# 5. Search Logic
recipes_list = [tea, coffee, cake, banana_smoothie]

ingredients_to_search = ["Water", "Sugar", "Bananas"]

for ingredient in ingredients_to_search:
    recipe_search(recipes_list, ingredient)
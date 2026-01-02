from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import or_

# --- Part 1: Setup & SQLAlchemy ---
# Connect using your credentials: cfpython / Khadijah1!
engine = create_engine("mysql+mysqlconnector://cfpython:Khadijah1!@localhost/task_database")

# Create the session
Session = sessionmaker(bind=engine)
session = Session()

# Create the declarative base
Base = declarative_base()

# --- Part 2: Model Definition ---
class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return f"<Recipe(id={self.id}, name={self.name}, difficulty={self.difficulty})>"

    def __str__(self):
        return (
            f"\n{'='*40}\n"
            f"Recipe ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Cooking Time: {self.cooking_time} mins\n"
            f"Difficulty: {self.difficulty}\n"
            f"Ingredients: {self.ingredients}\n"
            f"{'='*40}"
        )

    def calculate_difficulty(self):
        # Calculate based on cooking_time (int) and ingredients (list count)
        # We need to split the ingredients string to count them first
        ing_list = self.return_ingredients_as_list()
        num_ingredients = len(ing_list)

        if self.cooking_time < 10 and num_ingredients < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and num_ingredients >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and num_ingredients < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and num_ingredients >= 4:
            self.difficulty = "Hard"

    def return_ingredients_as_list(self):
        if not self.ingredients:
            return []
        return self.ingredients.split(", ")

# Create the table in the database
Base.metadata.create_all(engine)


# --- Part 3: Operations ---

def create_recipe():
    print("\n--- Create New Recipe ---")
    
    # 1. Name Validation
    name = input("Enter recipe name (max 50 chars): ")
    if len(name) > 50 or not name.replace(" ", "").isalnum():
        print("Invalid name. Must be alphanumeric and under 50 characters.")
        return

    # 2. Cooking Time Validation
    cooking_time_input = input("Enter cooking time (mins): ")
    if not cooking_time_input.isnumeric():
        print("Invalid time. Must be a number.")
        return
    cooking_time = int(cooking_time_input)

    # 3. Ingredients Collection
    ingredients = []
    try:
        num_ingredients = int(input("How many ingredients do you want to add? "))
        for i in range(num_ingredients):
            ing = input(f"Enter ingredient {i+1}: ")
            ingredients.append(ing)
    except ValueError:
        print("Invalid number.")
        return

    ingredients_str = ", ".join(ingredients)

    # 4. Create Object & Calculate Difficulty
    recipe_entry = Recipe(
        name=name,
        ingredients=ingredients_str,
        cooking_time=cooking_time
    )
    recipe_entry.calculate_difficulty()

    # 5. Add to DB
    session.add(recipe_entry)
    session.commit()
    print("Recipe added successfully!")


def view_all_recipes():
    print("\n--- All Recipes ---")
    recipes = session.query(Recipe).all()
    
    if not recipes:
        print("There are no recipes in the database.")
        return None

    for recipe in recipes:
        print(recipe)


def search_by_ingredients():
    # Check if DB is empty
    if session.query(Recipe).count() == 0:
        print("No recipes to search.")
        return

    # Get all unique ingredients
    results = session.query(Recipe.ingredients).all()
    all_ingredients = []
    
    for row in results:
        # row is a tuple like ('Sugar, Water',)
        ing_list = row[0].split(", ")
        for ing in ing_list:
            if ing not in all_ingredients:
                all_ingredients.append(ing)

    # Display numbered list
    print("\nAvailable Ingredients:")
    for i, ing in enumerate(all_ingredients):
        print(f"{i+1}. {ing}")

    # User Selection
    try:
        choices = input("\nEnter numbers of ingredients to search (space-separated, e.g., '1 3'): ").split()
        search_ingredients = []
        for c in choices:
            index = int(c) - 1
            # Validation
            if 0 <= index < len(all_ingredients):
                search_ingredients.append(all_ingredients[index])
            else:
                print(f"Number {c} is out of range.")
                return
    except ValueError:
        print("Invalid input.")
        return

    # Build Search Conditions
    conditions = []
    for term in search_ingredients:
        conditions.append(Recipe.ingredients.like(f"%{term}%"))

    # Execute Search (OR logic: recipes containing ANY of the terms)
    # Note: Instructions imply finding recipes that match *the criteria*. 
    # Usually "OR" is safer for "search by ingredients", but checking 'conditions' list.
    found_recipes = session.query(Recipe).filter(or_(*conditions)).all()

    if found_recipes:
        print(f"\nFound {len(found_recipes)} recipes:")
        for recipe in found_recipes:
            print(recipe)
    else:
        print("No matching recipes found.")


def edit_recipe():
    if session.query(Recipe).count() == 0:
        print("No recipes to edit.")
        return

    # List ID and Name
    results = session.query(Recipe).all()
    for recipe in results:
        print(f"ID: {recipe.id} - {recipe.name}")

    try:
        recipe_id = int(input("\nEnter ID of recipe to edit: "))
        recipe_to_edit = session.query(Recipe).filter(Recipe.id == recipe_id).first()

        if not recipe_to_edit:
            print("Recipe ID not found.")
            return

        print(f"\n1. Name ({recipe_to_edit.name})")
        print(f"2. Ingredients ({recipe_to_edit.ingredients})")
        print(f"3. Cooking Time ({recipe_to_edit.cooking_time})")
        
        choice = input("Enter number of attribute to edit: ")

        if choice == '1':
            new_name = input("Enter new name: ")
            if len(new_name) > 50:
                print("Name too long.")
                return
            recipe_to_edit.name = new_name

        elif choice == '2':
            # Simplified for UX: Re-enter all ingredients
            new_ings = []
            n = int(input("How many ingredients? "))
            for i in range(n):
                new_ings.append(input(f"Ing {i+1}: "))
            recipe_to_edit.ingredients = ", ".join(new_ings)
            recipe_to_edit.calculate_difficulty()

        elif choice == '3':
            new_time = input("Enter new cooking time: ")
            if not new_time.isnumeric():
                print("Invalid number.")
                return
            recipe_to_edit.cooking_time = int(new_time)
            recipe_to_edit.calculate_difficulty()

        else:
            print("Invalid choice.")
            return

        session.commit()
        print("Recipe updated!")

    except ValueError:
        print("Invalid input.")


def delete_recipe():
    if session.query(Recipe).count() == 0:
        print("No recipes to delete.")
        return

    # List ID and Name
    results = session.query(Recipe).all()
    for recipe in results:
        print(f"ID: {recipe.id} - {recipe.name}")

    try:
        recipe_id = int(input("\nEnter ID to delete: "))
        recipe_to_delete = session.query(Recipe).filter(Recipe.id == recipe_id).first()

        if not recipe_to_delete:
            print("ID not found.")
            return

        confirm = input(f"Are you sure you want to delete '{recipe_to_delete.name}'? (yes/no): ")
        if confirm.lower() == 'yes':
            session.delete(recipe_to_delete)
            session.commit()
            print("Recipe deleted.")
        else:
            print("Deletion cancelled.")

    except ValueError:
        print("Invalid input.")


# --- Part 4: Main Menu ---

def main_menu():
    while True:
        print("\n" + "*"*30)
        print("Main Menu")
        print("*"*30)
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for recipes by ingredients")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("Type 'quit' to exit.")

        choice = input("\nYour choice: ")

        if choice == '1':
            create_recipe()
        elif choice == '2':
            view_all_recipes()
        elif choice == '3':
            search_by_ingredients()
        elif choice == '4':
            edit_recipe()
        elif choice == '5':
            delete_recipe()
        elif choice.lower() == 'quit':
            print("Closing application...")
            session.close()
            engine.dispose()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
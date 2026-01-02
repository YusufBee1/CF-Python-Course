import mysql.connector

# --- Part 1: Database Setup ---
conn = mysql.connector.connect(
    host='localhost',
    user='cfpython',        # UPDATED: Matches your new MySQL username
    passwd='Khadijah1!'     # UPDATED: Matches your new MySQL password
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Recipes(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        ingredients VARCHAR(255),
        cooking_time INT,
        difficulty VARCHAR(20)
    )
''')

# --- Helper Function: Calculate Difficulty ---
def calculate_difficulty(cooking_time, ingredients):
    # Determine difficulty based on cooking time and ingredient count
    # ingredients is a list here
    num_ingredients = len(ingredients)
    
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    elif cooking_time >= 10 and num_ingredients >= 4:
        return "Hard"

# --- Part 3: Create Recipe ---
def create_recipe(conn, cursor):
    print("\n--- Create New Recipe ---")
    name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time (mins): "))
    ingredients_input = input("Enter ingredients (comma-separated, e.g. Sugar, Water): ")
    
    # Convert string input to list for calculation
    ingredients = ingredients_input.split(", ")
    
    difficulty = calculate_difficulty(cooking_time, ingredients)
    
    # Convert list back to string for SQL storage
    ingredients_str = ", ".join(ingredients)
    
    sql = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    val = (name, ingredients_str, cooking_time, difficulty)
    
    cursor.execute(sql, val)
    conn.commit()
    print("Recipe saved successfully!")

# --- Part 4: Search Recipe ---
def search_recipe(conn, cursor):
    print("\n--- Search Recipe ---")
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
    
    if not results:
        print("No recipes found to search.")
        return

    # Build unique ingredients list
    all_ingredients = []
    for row in results:
        # row[0] is the ingredient string "Sugar, Water"
        ing_list = row[0].split(", ")
        for ing in ing_list:
            if ing not in all_ingredients:
                all_ingredients.append(ing)

    # Display ingredients with index
    print("Available Ingredients:")
    for idx, ing in enumerate(all_ingredients):
        print(f"{idx}: {ing}")
    
    try:
        choice = int(input("Enter the number of the ingredient to search: "))
        search_term = all_ingredients[choice]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    # SQL LIKE Search
    sql = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
    val = (f"%{search_term}%",)
    
    cursor.execute(sql, val)
    results = cursor.fetchall()
    
    print(f"\nResults for '{search_term}':")
    for row in results:
        print(f"ID: {row[0]} | Name: {row[1]} | Time: {row[3]} | Diff: {row[4]} | Ingredients: {row[2]}")

# --- Part 5: Update Recipe ---
def update_recipe(conn, cursor):
    print("\n--- Update Recipe ---")
    # Show all recipes first
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()
    
    if not results:
        print("No recipes to update.")
        return

    for row in results:
        print(f"ID: {row[0]} | Name: {row[1]} | Ingredients: {row[2]} | Time: {row[3]}")
    
    try:
        recipe_id = int(input("Enter the ID of the recipe to update: "))
        column_to_update = input("Which column (name, cooking_time, ingredients)? ").lower()
        
        # Valid column check
        if column_to_update not in ['name', 'cooking_time', 'ingredients']:
            print("Invalid column.")
            return

        new_value = input(f"Enter new value for {column_to_update}: ")
        
        # Special logic: If updating time or ingredients, recalculate difficulty
        if column_to_update == 'cooking_time':
            new_value = int(new_value)
            # Need to fetch current ingredients to calc difficulty
            cursor.execute("SELECT ingredients FROM Recipes WHERE id = %s", (recipe_id,))
            current_ingredients = cursor.fetchone()[0].split(", ")
            new_difficulty = calculate_difficulty(new_value, current_ingredients)
            
            # Update both time and difficulty
            cursor.execute("UPDATE Recipes SET cooking_time = %s, difficulty = %s WHERE id = %s", (new_value, new_difficulty, recipe_id))

        elif column_to_update == 'ingredients':
            # Need to fetch current time to calc difficulty
            cursor.execute("SELECT cooking_time FROM Recipes WHERE id = %s", (recipe_id,))
            current_time = cursor.fetchone()[0]
            new_ingredients_list = new_value.split(", ")
            new_difficulty = calculate_difficulty(current_time, new_ingredients_list)
            
            # Update both ingredients and difficulty
            cursor.execute("UPDATE Recipes SET ingredients = %s, difficulty = %s WHERE id = %s", (new_value, new_difficulty, recipe_id))
            
        else:
            # Simple update for name
            sql = f"UPDATE Recipes SET {column_to_update} = %s WHERE id = %s"
            cursor.execute(sql, (new_value, recipe_id))

        conn.commit()
        print("Update successful!")
        
    except ValueError:
        print("Invalid input.")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Part 6: Delete Recipe ---
def delete_recipe(conn, cursor):
    print("\n--- Delete Recipe ---")
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()
    
    if not results:
        print("No recipes to delete.")
        return

    for row in results:
        print(f"ID: {row[0]} | Name: {row[1]}")
        
    try:
        recipe_id = int(input("Enter ID to delete: "))
        cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id,))
        conn.commit()
        print("Recipe deleted.")
    except Exception as e:
        print(f"Error: {e}")

# --- Part 2: Main Menu ---
def main_menu(conn, cursor):
    while True:
        print("\n--- Main Menu ---")
        print("1. Create a Recipe")
        print("2. Search for a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        elif choice == '5':
            conn.commit()
            conn.close()
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu(conn, cursor)
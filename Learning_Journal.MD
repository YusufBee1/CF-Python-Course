# Learning Journal

## Exercise 1.1 - Python Setup
**Date:** December 2025

**Experience:**
Coming from a JavaScript/React background, setting up Python felt a bit different. I learned about the importance of Python versions (3.8 vs 3.13) and how data science libraries can be picky about "bleeding edge" updates.

**What I Learned:**
* How to install specific Python versions using `winget` to avoid "End of Life" web warnings.
* The difference between `pip freeze` (exporting) and `pip install -r` (importing) for sharing environments.
* How to manage multiple Python versions on Windows using the Python Launcher (`py`).

**Goals:**
I want to master Python's data analysis libraries to complement my front-end skills.

# Learning Journal - Exercise 1.2

**Date:** December 2025

**What I Learned:**
* **Dictionaries vs. Lists:** Coming from JavaScript, I realized that Python's Dictionaries are very similar to JS Objects (key-value pairs), while Lists are essentially Arrays.
* **Mutability:** Both structures are mutable, meaning I can add recipes to my list or change ingredients in a dictionary after they are created.
* **Iteration:** Using a `for` loop in Python is cleaner and more readable than the traditional `for(i=0;...)` loops I'm used to in other languages.

# Learning Journal - Exercise 1.3
**Experience:**
This was the first step into actual logic programming. I learned how to bridge the gap between user input (which is always a string) and the data types I need (integers and lists).

**Key Takeaway:**
The `.split(", ")` method is crucial for parsing comma-separated lists from users. I also got comfortable using complex `if/elif` structures to create logic gates for the difficulty ratings.

# Learning Journal - Exercise 1.4
**Date:** December 2025

**Experience:**
This exercise was a significant step up because I moved from working with temporary data (variables) to persistent data (files). Building a program that "remembers" recipes after it closes felt like building a real application.

**What I Learned:**
* **The Pickle Module:** I learned how to use `pickle` to serialize Python objects (like dictionaries and lists) into binary files so they can be stored and retrieved later.
* **Binary Modes:** I understood the difference between writing text (`w`) and writing binary (`wb`), which is crucial for non-text data.
* **Exception Handling:** I used `try`, `except`, `else`, and `finally` blocks to make the code robust. This prevents the program from crashing if a file is missing or user input is invalid.

**Challenges:**
It was tricky to manage the logic flow of opening a file, loading data, modifying it, and then saving it back without overwriting or losing existing data.

# Learning Journal - Exercise 1.5
**Date:** December 2025

**Experience:**
This exercise introduced Object-Oriented Programming (OOP). Instead of managing separate lists and dictionaries, I created a `Recipe` class that holds both data (attributes) and behavior (methods).

**What I Learned:**
* **Classes vs. Objects:** The Class `Recipe` is the blueprint, while `tea` and `coffee` are specific instances (Objects) built from that blueprint.
* **The `self` keyword:** I learned that `self` allows the code to distinguish between *this* specific recipe's name and *that* recipe's name.
* **Magic Methods:** I used `__init__` to set up the object and `__str__` to define how the object looks when printed.
* **Variable Arguments:** Using `*args` in `add_ingredients` was cool—it let me pass as many ingredients as I wanted without creating a list first.

# Learning Journal - Exercise 1.6
**Date:** January 2026

**Experience:**
This was the most complex task yet. I successfully connected a Python script to a MySQL database using the `mysql-connector-python` library.

**What I Learned:**
* **Database Connections:** I learned that Python needs a specific "driver" (connector) to talk to a database server.
* **SQL in Python:** I practiced writing SQL queries (`INSERT`, `SELECT`, `UPDATE`, `DELETE`) inside Python strings and executing them with a cursor.
* **Environment Setup:** The biggest challenge was realizing I needed the actual MySQL Server software installed and running on my machine, not just the Python library. I had to configure a specific user and password to match my script.

**Challenges:**
Setting up the local MySQL server and ensuring the user credentials (`cfpython`) matched my code exactly was a major troubleshooting step.

# Learning Journal - Exercise 1.7
**Date:** January 2026

**Experience:**
This final task brought everything together. I built a complete command-line application that uses Object-Relational Mapping (ORM) with SQLAlchemy. It felt much more professional than writing raw SQL strings.

**What I Learned:**
* **SQLAlchemy ORM:** I learned how to define a database schema using Python Classes (`DeclarativeBase`). This makes the code cleaner because I'm working with Objects (like `Recipe`) rather than raw database tuples.
* **Logic & Validation:** I implemented robust input handling—checking for alphanumeric names, valid integers for cooking times, and ensuring users can't crash the app with bad inputs.
* **Complex Searching:** The `search_by_ingredients` function was challenging. I had to retrieve strings, split them into lists, display them uniquely, and then build a dynamic SQL query using the `.like()` operator.

**Challenges:**
Transitioning from raw SQL (in 1.6) to SQLAlchemy (in 1.7) required a shift in thinking. Instead of writing `INSERT INTO`, I had to think about creating an Object and `session.add()`-ing it. Managing the session flow (commits and closes) was also critical to prevent database locks.

# Learning Journal - Exercise 2.1
**Date:** January 2026

**Experience:**
This was my introduction to Web Development with Python. I spent time researching the Django framework to understand why major companies like Instagram and Spotify use it. I also set up my first "practice" environment to get comfortable with the installation process before starting the main project.

**What I Learned:**
* **Django's Philosophy:** I learned that Django is "batteries-included," meaning it comes with built-in tools for authentication, database management, and security. This makes it ideal for complex, user-heavy applications but overkill for simple static sites.
* **Virtual Environments:** I practiced creating and activating a specific virtual environment (`achievement2-practice`) to keep my Django installation isolated from my system Python.
* **Installation Checks:** I learned how to verify my installation using `python -m django --version` to ensure the framework is ready to use.

# Learning Journal - Exercise 2.2
**Date:** January 2026

**Experience:**
In this exercise, I officially started the Django Recipe Application. I moved from simple Python scripts to a full web framework structure. I set up the project foundation, configured the virtual environment, and accessed the Django Admin interface for the first time.

**What I Learned:**
* **Project Structure:** I learned how `django-admin startproject` generates the initial file structure (like `manage.py`, `settings.py`, and `urls.py`) and why the containing folder needs to be distinct from the project package.
* **Virtual Environments:** I reinforced the importance of creating a fresh virtual environment (`a2-ve-recipeapp`) for each new major project to manage dependencies cleanly.
* **The "Migrate" Command:** I learned that `python manage.py migrate` is necessary to initialize the database (SQLite by default) before the app can actually run.
* **Superuser:** I discovered how to create an admin account (`createsuperuser`) to access the built-in Django back-end, which provides a powerful GUI for managing users and data right out of the box.

**Challenges:**
The renaming step (changing `recipe_project` to `src`) was a specific structural requirement that required careful navigation in the file system to ensure I didn't break the path to `manage.py`.

# Learning Journal - Exercise 2.3
**Date:** January 2026

**Experience:**
This exercise was the "construction phase" of the Recipe App. I moved from setup to actually building the core features. I designed the database schema, created the `recipes` app, defined the data model in Python code, and successfully migrated it to the database. I also navigated the complexity of managing two separate GitHub repositories—one for the course deliverables and a new dedicated one for the app code.

**What I Learned:**
* **Models as Blueprints:** I learned that a Django Model (`class Recipe(models.Model)`) is the single source of truth for your data. You define it in Python, and Django handles the SQL behind the scenes.
* **The Migration Workflow:** I practiced the two-step process: `makemigrations` (prepare the changes) and `migrate` (apply them to the DB).
* **Django Admin:** I saw how registering a model in `admin.py` instantly creates a professional CRUD (Create, Read, Update, Delete) interface without writing any HTML.
* **Nested Repositories:** I learned how to initialize a fresh git repository inside a subfolder (`src`) to track the application code separately from my course coursework.

**Challenges:**
The most complex part was managing the folder structures and ensuring I was in the correct directory for specific commands. Understanding where `settings.py` lives versus where the `apps` live took some getting used to.

# Learning Journal - Exercise 2.4
**Date:** January 2026

**Experience:**
This exercise was my first foray into the "Frontend" of Django. I moved beyond the Admin panel and created my first public-facing view. I designed a simple HTML Welcome page and learned how to "wire" it up using Django's URL routing system.

**What I Learned:**
* **MVT Architecture:** I learned how Model-View-Template works in practice. The View (`views.py`) fetches the data (or in this case, simply loads the page), and the Template (`.html`) displays it.
* **Template Namespacing:** I learned why we create a folder structure like `templates/recipes/home.html`—it prevents naming conflicts if multiple apps have a file named `home.html`.
* **URL Chaining:** I understood how the main `recipe_project/urls.py` delegates traffic to the specific `recipes/urls.py` using the `include()` function.

**Challenges:**
The folder structure for templates is a bit nested (`recipes/templates/recipes`), which feels redundant at first but makes sense for organizing larger projects.

# Learning Journal - Exercise 2.6
**Date:** January 2026

**Experience:**
In this exercise, I implemented the security layer of the application. I built a Login and Logout system using Django's built-in authentication tools. I learned how to protect specific views so that only logged-in users can access the recipe content, while keeping the "Home" page public.

**What I Learned:**
* **The `@login_required` Decorator:** I learned how adding this single line above a function protects the entire view.
* **Django's Auth System:** I used `AuthenticationForm` to handle the UI and `login()`/`logout()` functions to manage the user's session.
* **The `?next=` Parameter:** I saw how Django remembers where the user *wanted* to go (e.g., `/list/`), sends them to login, and then redirects them back to their destination automatically.

**Challenges:**
I encountered a `Page not found (404)` error where Django was trying to redirect unauthorized users to `/accounts/login/` by default. I learned that I had to explicitly define `LOGIN_URL = '/login/'` in `settings.py` to tell Django to use my custom login route instead.
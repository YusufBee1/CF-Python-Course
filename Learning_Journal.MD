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
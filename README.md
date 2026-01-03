# Exercise 1.1: Python Installation & Setup

## Description
This is the first exercise for the CareerFoundry Python Specialization. The goal was to install Python, set up a virtual environment, and run a basic script.

## Installation Steps
1. Installed Python 3.8.7 (via winget/installer).
2. Created a virtual environment `cf-python-base`.
3. Installed `ipython` and generated `requirements.txt`.
4. Verified reproducibility by creating a second environment `cf-python-copy`.

## Files Included
* `add.py`: A script that adds two user-inputted numbers.
* `requirements.txt`: List of dependencies (ipython).
* Screenshots of the installation and verification process.

# Exercise 1.2: Data Structures in Python

## Description
This exercise focuses on creating and manipulating fundamental Python data structures: Dictionaries and Lists.

## Data Structure Choices

### 1. The Recipe Structure (`recipe_1`)
I chose a **Dictionary** for the individual recipes. Dictionaries are ideal for storing data as key-value pairs (`name`, `cooking_time`, `ingredients`), which allows for clear labeling of each attribute. This structure makes it easy to access specific details (like just the ingredients) by referencing the key name, rather than relying on a numeric index.

### 2. The Outer Structure (`all_recipes`)
I chose a **List** for the outer structure to hold the recipes. Lists are sequential and ordered, which is perfect for maintaining a collection of items. A list allows us to easily iterate through the recipes (as shown in the ingredients loop) and dynamically add or remove recipes using methods like `.append()`, making it a flexible choice for a growing dataset.

# Exercise 1.3: Control Flow & Loops

## Description
This script is a dynamic recipe intake tool. It demonstrates the use of:
* **While/For Loops:** To iterate through user input.
* **Logical Operators (and/or):** To calculate recipe difficulty based on multiple conditions (cooking time + ingredient count).
* **Data sanitization:** Using `.split()` to convert raw string input into usable lists.

# Recipe App 🍳

A web-based recipe application built with Django (Python) that allows users to view, search, and manage recipes. The application includes authentication, data visualization using Pandas/Matplotlib, and a responsive design.

## 🚀 Live Demo
**View the live application here:** [https://yusuf-recipe-app-e9b7920225a4.herokuapp.com/](https://yusuf-recipe-app-e9b7920225a4.herokuapp.com/)

## 🛠 Technologies Used
* **Backend:** Django, Python
* **Database:** PostgreSQL (Production), SQLite (Development)
* **Frontend:** HTML5, CSS3, JavaScript
* **Data Analysis:** Pandas, Matplotlib (for generating recipe difficulty charts)
* **Hosting:** Heroku (using Gunicorn & Whitenoise)

## ✨ Features
* **User Authentication:** Secure login/logout for users.
* **Recipe Management:** Users can add new recipes.
* **Search Functionality:** Search recipes by name or ingredients.
* **Data Visualization:** Dynamic charts showing cooking time trends and difficulty distribution.
* **Responsive Design:** Optimized for mobile and desktop viewing.

## 🔧 How to Run Locally
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YusufBee1/recipe-app.git](https://github.com/YusufBee1/recipe-app.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd recipe-app
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run migrations:**
    ```bash
    python manage.py migrate
    ```
5.  **Start the server:**
    ```bash
    python manage.py runserver
    ```
6.  **Access the app:** Open `http://127.0.0.1:8000/` in your browser.

## 🧪 Testing
To run the automated tests for this application:
```bash
python manage.py test
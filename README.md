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
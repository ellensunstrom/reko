# first try
from recipe import *
from recipeManager import *

recipe_manager = RecipeManager()

def add_recipe():
    print("CREATE NEW RECIPE")
    title = read_input("Title: ")
    description = input("Description (optinal): ")
    ingredients = read_input("Ingredients: ")
    instructions = read_input("Instructions: ")
    new_recipe = Recipe(title, description, ingredients, instructions)
    added = recipe_manager.add(new_recipe)
    if added:
        print("RECIPE ADDED")
    else:
        print ("UNABLE TO ADD RECIPE")

def read_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip() != "":
            return user_input
        print("Incorrect input.")

def show_recipe_list():
    print("\n--: YOUR RECIPE COLLECTION :--\n")
    list_of_titles = recipe_manager.list_to_string()
    if list_of_titles == "":
        print("The recipe collection is empty!")
    else:
        print(list_of_titles)
    # TODO show submenu?

def show_menu():
    print("What do you wish to do?")
    print("s) Show recipe list")
    print("r) Show a specific recipe")
    print("n) Add new recipe")
    print("q) Quit")

def main_loop():
    show_menu()
    choice = input("Selection: ").strip().lower()
    match choice:
        case "s": # Show recipe list
            show_recipe_list()
            
        case "r": # Show recipe
            pass
        case "n": # Add recipe
            add_recipe()
        case "q": # Quit
            print("Bye!")
            keep_going = False  # TODO Why doesn't this work to break the loop?


spags = Recipe("spago", "", "2 spags", "boil spag")
print(spags.ingredients)
recipe_manager.add(spags)

print("Welcome to REKO - Your recipe collection!")


# Keep this at the bottom!
keep_going = True
while keep_going:
    main_loop()

""" 
Recipe
Recipe Manager
main loop
- save to file
- load file
- add recipe
- view recipe
- edit recipe
category enum?



 """


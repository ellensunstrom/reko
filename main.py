# first try
from recipe import *
from recipeManager import *

recipe_manager = RecipeManager()

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
            pass
        case "r": # Show recipe
            pass
        case "n": # Add recipe
            pass
        case "q": # Quit
            print("Bye!")
            keep_going = False  # TODO Why doesn't this work to break the loop?


spags = Recipe("spago", "", "2 spags", "boil spag")
print(spags.ingredients)

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


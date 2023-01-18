
class RecipeManager:
    
    
    def __init__(self):
       self.recipe_list = []
    
    def __str__(self):
        if len(self.recipe_list) != 0:
            str_list = ''
            for recipe in self.recipe_list:
                number = self.recipe_list(recipe)
                str_list += "{number})  {recipe.title}"
            str_list += ''
            return str_list
        return "The recipe collection is empty!"

# TODO check list for title, do not add if title already present
# TODO add in alphabetical order
    def add(self, recipe):
        self.recipe_list.append(recipe)
        return True
    
    def get_recipe():
        pass
    
    def remove_recipe(recipe):
        return False
    
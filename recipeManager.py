
class RecipeManager:
    
    
    def __init__(self):
       self.recipe_list = []


    # TODO check list for title, do not add if title already present
    # TODO add in alphabetical order
    def add(self, recipe):
        self.recipe_list.append(recipe)
        return True
    
    # TODO
    def get_recipe(self):
        pass

    # TODO
    def remove_recipe(self, recipe):
        return False

    def list_to_string(self):
        if len(self.recipe_list) != 0:
            str_list = ''
            for recipe in self.recipe_list:
                number = self.recipe_list.index(recipe) + 1
                str_list += f"{number}:  {recipe.title}\n"
            str_list += ''
            return str_list
        return ""
    
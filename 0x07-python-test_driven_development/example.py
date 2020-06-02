class Pokemon:
    number_of_pokemons = 0

    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

a = 5



from ex0.abstract_creatures import CreatureFactory, Creature


class Flameling(Creature):

    def attack(self):
        return f"{self.__class__.__name__} uses Ember!"

    def describe(self):
        return super().describe()


class Pyrodon(Creature):

    def attack(self):
        return f"{self.__class__.__name__} uses a Flamethrower!"

    def describe(self):
        return super().describe()

class Aquabub(Creature):

    def attack(self):
        return f"{self.__class__.__name__} uses Water Gun!"

    def describe(self):
        return super().describe()

class Torragon(Creature):

    def attack(self):
        return f"{self.__class__.__name__} uses Hydro Pump!"

    def describe(self):
        return super().describe()

from abc import abstractmethod, ABC


class Creature(ABC):

    def __init__(self, name: str, type_creature: str):
        self.name = name
        self.type_creature = type_creature

    @abstractmethod
    def attack(self):
        pass

    def describe(self):
        return f"{self.name} is a {self.type_creature} type Creature"

class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self):
        pass

    @abstractmethod
    def create_evolved(self):
        pass

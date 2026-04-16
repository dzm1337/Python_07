from ex0.concrete_creatures import Flameling, Pyrodon, Aquabub, Torragon
from ex0.abstract_creatures import CreatureFactory, Creature


class FlameFactory(CreatureFactory):

    def create_base(self) -> Creature:
        flameling = Flameling("Flameling", "Fire")
        return flameling
    
    def create_evolved(self) -> Creature:
        pyrodon = Pyrodon("Pyrodon", "Fire/Flying")
        return pyrodon


class WaterFactory(CreatureFactory):

    def create_base(self) -> Creature:
        aquabub = Aquabub("Aquabub", "Water")
        return aquabub
    
    def create_evolved(self) -> Creature:
        torragon = Torragon("Torragon", "Water")
        return torragon

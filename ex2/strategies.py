from ex0 import Creature
from ex1 import (
    HealCapability,
    HealingCreatureFactory,
    Morphagon,
    Shiftling,
    Sproutling,
    TransformCapability,
    TransformCreatureFactory,
)

from ex2 import BattleError, BattleStrategy


class NormalStrategy(BattleStrategy):
    def __init__(self, creature: Creature) -> None:
        BattleStrategy.__init__(self, creature)

    def is_valid(self) -> bool:
        return isinstance(self.creature, Creature)

    def act(self) -> None:
        if not self.is_valid():
            raise BattleError(self.creature, self.__class__)
        self.creature.attack()


class AggressiveStrategy(BattleStrategy):
    def __init__(self, creature: Creature) -> None:
        BattleStrategy.__init__(self, creature)

    def is_valid(self) -> bool:
        return isinstance(self.creature, TransformCapability)

    def act(self) -> None:
        if not self.is_valid():
            raise BattleError(self.creature, self.__class__)
        factory = TransformCreatureFactory()
        if isinstance(self.creature, Shiftling):
            creature = factory.create_base()
        elif isinstance(self.creature, Morphagon):
            creature = factory.create_evolved()
        creature.attack()
        creature.transform()
        creature.attack()
        creature.revert()


class DefensiveStrategy(BattleStrategy):
    def __init__(self, creature: Creature) -> None:
        BattleStrategy.__init__(self, creature)

    def is_valid(self) -> bool:
        return isinstance(self.creature, HealCapability)

    def act(self) -> None:
        if not self.is_valid():
            raise BattleError(self.creature, self.__class__)
        factory = HealingCreatureFactory()
        if isinstance(self.creature, Sproutling):
            creature = factory.create_base()
        elif isinstance(self.creature, Morphagon):
            creature = factory.create_evolved()
        creature.attack()
        creature.heal()

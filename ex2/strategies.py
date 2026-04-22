from ex0.abstract_creatures import Creature
from ex2.abstract_strategy import BattleError, BattleStrategy
from ex1.capabilities import TransformCapability, HealCapability

class NormalStrategy(BattleStrategy):
    def __init__(self, creature: Creature) -> None:
        BattleStrategy.__init__(self, creature)

    def is_valid(self, creature : Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise BattleError(creature, self.__class__)
        creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise BattleError(creature, self.__class__)
        creature.attack()
        creature.transform()
        creature.attack()
        creature.revert()


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise BattleError(creature, self.__class__)
        creature.attack()
        creature.heal()

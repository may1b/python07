from abc import ABC, abstractmethod

from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability


class StrategyError(Exception):
    pass


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        raise NotImplementedError

    @abstractmethod
    def act(self, creature: Creature) -> None:
        raise NotImplementedError


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            desc = type(self).__name__[:-len("Strategy")].lower()
            raise StrategyError(
                f"Invalid Creature '{creature.name}' for this {desc} strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, HealCapability):
            desc = type(self).__name__[:-len("Strategy")].lower()
            raise StrategyError(
                f"Invalid Creature '{creature.name}' for this {desc} strategy"
            )
        print(creature.attack())
        print(creature.heal())


__all__: list[str] = [
    "StrategyError",
    "BattleStrategy",
    "NormalStrategy",
    "AggressiveStrategy",
    "DefensiveStrategy",
]

from ex0.factory import CreatureFactory
from ex1.creature import (
    Bloomelle,
    HealingCreature,
    Morphagon,
    Shiftling,
    Sproutling,
    TransformingCreature,
)


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> HealingCreature:
        return Sproutling()

    def create_evolved(self) -> HealingCreature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> TransformingCreature:
        return Shiftling()

    def create_evolved(self) -> TransformingCreature:
        return Morphagon()


__all__: list[str] = [
    "HealingCreatureFactory",
    "TransformCreatureFactory",
]

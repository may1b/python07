from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.creature import HealingCreature, TransformingCreature


def test_healing_factory(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print("base:")
    base: HealingCreature = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print("evolved:")
    evolved: HealingCreature = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform_factory(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    print("base:")
    base: TransformingCreature = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print("evolved:")
    evolved: TransformingCreature = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def main() -> None:
    healing_factory = HealingCreatureFactory()
    test_healing_factory(healing_factory)
    transform_factory = TransformCreatureFactory()
    test_transform_factory(transform_factory)


if __name__ == "__main__":
    main()

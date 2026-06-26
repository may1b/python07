from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    NormalStrategy,
    StrategyError,
)


Opponent = tuple[CreatureFactory, BattleStrategy]


def factory_label(factory: CreatureFactory) -> str:
    cls_name = type(factory).__name__
    if cls_name.endswith("CreatureFactory"):
        return cls_name[:-len("CreatureFactory")]
    return factory.create_base().name


def strategy_label(strategy: BattleStrategy) -> str:
    return type(strategy).__name__[:-len("Strategy")]


def format_opponents(opponents: list[Opponent]) -> str:
    parts = [
        f"({factory_label(f)}+{strategy_label(s)})"
        for f, s in opponents
    ]
    return "[ " + ", ".join(parts) + " ]"


def battle(first: Opponent, second: Opponent) -> bool:
    first_factory, first_strategy = first
    second_factory, second_strategy = second
    first_creature = first_factory.create_base()
    second_creature = second_factory.create_base()
    print("* Battle *")
    print(first_creature.describe())
    print("vs.")
    print(second_creature.describe())
    print("now fight!")
    try:
        first_strategy.act(first_creature)
        second_strategy.act(second_creature)
    except StrategyError as error:
        print(f"Battle error, aborting tournament: {error}")
        return False
    return True


def run_tournament(index: int, name: str, opponents: list[Opponent]) -> None:
    print(f"Tournament {index} ({name})")
    print(format_opponents(opponents))
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            if not battle(opponents[i], opponents[j]):
                return


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    tournaments: list[tuple[str, list[Opponent]]] = [
        (
            "basic",
            [
                (flame_factory, normal),
                (healing_factory, defensive),
            ],
        ),
        (
            "error",
            [
                (flame_factory, aggressive),
                (healing_factory, defensive),
            ],
        ),
        (
            "multiple",
            [
                (aqua_factory, normal),
                (healing_factory, defensive),
                (transform_factory, aggressive),
            ],
        ),
    ]

    for index, (name, opponents) in enumerate(tournaments):
        run_tournament(index, name, opponents)


if __name__ == "__main__":
    main()

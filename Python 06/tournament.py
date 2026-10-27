#!/usr/bin/env python3
from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4 import (AggressiveStrategy, BattleStrategy, DefensiveStrategy,
                 InvalidStrategyError, NormalStrategy)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    fighters = [(factory.create_base(), strategy)
                for factory, strategy in opponents]
    print("*** Tournament ***")
    print(f"{len(fighters)} opponents involved")
    try:
        # Cada oponente enfrenta cada outro exatamente uma vez (i < j)
        for i in range(len(fighters)):
            for j in range(i + 1, len(fighters)):
                first, first_strategy = fighters[i]
                second, second_strategy = fighters[j]
                print("\n* Battle *")
                print(first.describe())
                print(" vs.")
                print(second.describe())
                print(" now fight!")
                # O torneio NAO sabe a familia: cada estrategia decide
                first_strategy.act(first)
                second_strategy.act(second)
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


def label(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> str:
    parts = [f"({factory.create_base().name}+{strategy.name})"
             for factory, strategy in opponents]
    return "[ " + ", ".join(parts) + " ]"


def main() -> None:
    flame = FlameFactory()
    transform = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    tournaments: list[tuple[str,
                            list[tuple[CreatureFactory, BattleStrategy]]]] = [
        ("basic", [(flame, normal), (transform, aggressive)]),
        ("error", [(transform, aggressive), (flame, aggressive)]),
        ("multiple", [(flame, normal), (transform, aggressive),
                      (flame, defensive)]),
    ]
    for index, (title, opponents) in enumerate(tournaments):
        print(f"Tournament {index} ({title})")
        print(label(opponents))
        battle(opponents)
        print()


if __name__ == "__main__":
    main()

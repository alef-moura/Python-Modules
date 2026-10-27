#!/usr/bin/env python3
import random

ALL_ACHIEVEMENTS = [
    "First Steps", "Boss Slayer", "Master Explorer", "Collector Supreme",
    "Speed Runner", "Untouchable", "Crafting Genius", "World Savior",
    "Treasure Hunter", "Strategist", "Survivor", "Unstoppable",
    "Sharp Mind", "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    count = random.randint(7, 10)
    # random.sample escolhe 'count' itens diferentes da lista
    return set(random.sample(ALL_ACHIEVEMENTS, count))


def main() -> None:
    print("=== Achievement Tracker System ===")
    names = ["Alice", "Bob", "Charlie", "Dylan"]
    # Listas paralelas: achievements[i] pertence a names[i]
    achievements = [gen_player_achievements() for _ in names]

    index = 0
    for name in names:
        print(f"Player {name}: {achievements[index]}")
        index += 1

    every: set[str] = set()
    for player_set in achievements:
        every = every.union(player_set)  # uniao: tudo de todos
    print(f"\nAll distinct achievements: {every}")

    common = set(ALL_ACHIEVEMENTS)
    for player_set in achievements:
        common = common.intersection(player_set)  # o que todos tem
    print(f"\nCommon achievements: {common}\n")

    index = 0
    for name in names:
        others: set[str] = set()
        other_index = 0
        for other_set in achievements:
            if other_index != index:
                others = others.union(other_set)
            other_index += 1
        # diferenca: o que so este jogador tem
        print(f"Only {name} has: {achievements[index].difference(others)}")
        index += 1
    print()

    index = 0
    for name in names:
        missing = set(ALL_ACHIEVEMENTS).difference(achievements[index])
        print(f"{name} is missing: {missing}")
        index += 1


if __name__ == "__main__":
    main()

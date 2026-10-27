#!/usr/bin/env python3
from ex3 import Creature, TransformCapability, TransformCreatureFactory


def exercise(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    # isinstance verifica a CAPACIDADE, nao a familia concreta
    if isinstance(creature, TransformCapability):
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
    else:
        print(f"{creature.name} cannot transform.")


def main() -> None:
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()
    print("\n base:")
    exercise(factory.create_base())
    print("\n evolved:")
    exercise(factory.create_evolved())


if __name__ == "__main__":
    main()

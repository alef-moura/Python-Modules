from abc import ABC, abstractmethod

from .creature import Creature
from .flame import Flameling, Pyrodon
from .shapeshifter import Morphagon, Shiftling


class CreatureFactory(ABC):
    """Fabrica abstrata: quem usa nao precisa saber a classe concreta."""

    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()

from abc import ABC, abstractmethod


class TransformCapability(ABC):
    """Habilidade separada: NAO herda de Creature.

    So as criaturas que realmente sabem se transformar herdam desta classe.
    """

    def __init__(self) -> None:
        self._transformed = False

    def is_transformed(self) -> bool:
        return self._transformed

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...

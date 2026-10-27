# O pacote expoe apenas as fabricas e os tipos abstratos.
# As criaturas concretas (Flameling, Shiftling...) ficam escondidas.
from .capability import TransformCapability
from .creature import Creature
from .factory import CreatureFactory, FlameFactory, TransformCreatureFactory

__all__ = [
    "Creature",
    "TransformCapability",
    "CreatureFactory",
    "FlameFactory",
    "TransformCreatureFactory",
]

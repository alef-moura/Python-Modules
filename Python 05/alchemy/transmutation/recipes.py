# Import absoluto: caminho completo a partir da raiz do projeto
import elements
from alchemy.elements import create_air

# Import relativo: ".." sobe um nivel (de transmutation para alchemy)
from ..potions import strength_potion


def lead_to_gold() -> str:
    return ("Recipe transmuting Lead to Gold: brew "
            f"'{create_air()}' and '{strength_potion()}' mixed with "
            f"'{elements.create_fire()}'")

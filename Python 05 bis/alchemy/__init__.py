# O __init__.py e a "porta de entrada" do pacote: so o que for
# importado aqui fica visivel em "import alchemy".
from .elements import create_air

__all__ = ["create_air"]

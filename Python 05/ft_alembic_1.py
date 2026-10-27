#!/usr/bin/env python3
import alchemy

print("=== Alembic 1 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
print("Now show that not all functions can be reached")
print("This will raise an exception!")
print("Testing the hidden create_earth: ", end="", flush=True)
# Erro proposital (o mypy tambem reclama): create_earth nao e exposto
print(f"{alchemy.create_earth()}")

#!/usr/bin/env python3
import importlib
import sys
from types import ModuleType

# nome do pacote -> descricao exibida
REAGENTS = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
}


def load(name: str) -> ModuleType | None:
    try:
        # importlib permite importar um modulo a partir de uma string
        return importlib.import_module(name)
    except ImportError:
        return None


def main() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print()
    print("Checking dependencies:")
    missing: list[str] = []
    for name, description in REAGENTS.items():
        module = load(name)
        if module is None:
            print(f"[MISSING] {name} - not installed")
            missing.append(name)
        else:
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {name} ({version}) - {description}")

    print()
    print("pip vs Poetry:")
    print("requirements.txt declares what to install; pip resolves it at "
          "install time.")
    print("pyproject.toml declares the same constraints, and Poetry pins "
          "the resolved")
    print("versions in poetry.lock so every install is identical.")
    print()

    if missing:
        print(f"Missing reagents: {', '.join(missing)}")
        print("Install them with pip:")
        print("  pip install -r ex0/requirements.txt")
        print("Or with Poetry (from the ex0/ folder):")
        print("  poetry install")
        print("  poetry run python loading.py")
        return

    # Uso real dos dois reagentes juntos
    numpy = load("numpy")
    pandas = load("pandas")
    if numpy is not None and pandas is not None:
        values = numpy.array([1.0, 2.0, 3.0, 4.0])
        frame = pandas.DataFrame({"dose": values})
        print(f"Quick experiment: mean dose = {frame['dose'].mean()}")
    print(f"Running on Python {sys.version.split()[0]}")
    print("All reagents present and accounted for.")


if __name__ == "__main__":
    main()

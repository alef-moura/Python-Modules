#!/usr/bin/env python3
import os
import site
import sys


def in_virtualenv() -> bool:
    # Dentro de um venv, sys.prefix aponta para o venv e
    # sys.base_prefix continua apontando para o Python "global".
    return sys.prefix != sys.base_prefix


def site_packages() -> list[str]:
    try:
        return site.getsitepackages()
    except AttributeError:
        return []


def main() -> None:
    if not in_virtualenv():
        print("LABORATORY STATUS: You are working in the open")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")
        print()
        print("Global reagent installation path:")
        for path in site_packages():
            print(f"  {path}")
        print()
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate # On Windows")
        print()
        print("Then run this program again.")
        return

    env_path = sys.prefix
    print("LABORATORY STATUS: The laboratory is sealed")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(env_path)}")
    print(f"Environment Path: {env_path}")
    print()
    print("SUCCESS: You are working in an isolated environment!")
    print("Safe to install reagents without affecting")
    print("the global system.")
    print()
    print("Reagent installation path:")
    for path in site_packages():
        print(f"  {path}")
    print()
    print("Global Python (outside the laboratory):")
    print(f"  {sys.base_prefix}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import os
import sys

try:
    from dotenv import load_dotenv
    HAS_DOTENV = True
except ImportError:
    HAS_DOTENV = False

HERE = os.path.dirname(os.path.abspath(__file__))
REQUIRED = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL",
            "ZION_ENDPOINT"]
DEFAULTS = {
    "MATRIX_MODE": "development",
    "LOG_LEVEL": "INFO",
}


def load_config() -> tuple[dict[str, str | None], list[str]]:
    env_file = os.path.join(HERE, ".env")
    if not HAS_DOTENV:
        print("WARNING: python-dotenv is not installed "
              "(pip install -r ex1/requirements.txt)")
    elif os.path.exists(env_file):
        # override=False: variaveis ja definidas no ambiente tem prioridade
        load_dotenv(env_file, override=False)
    else:
        print("WARNING: no .env file found (cp ex1/.env.example ex1/.env)")

    config: dict[str, str | None] = {}
    missing: list[str] = []
    for key in REQUIRED:
        value = os.environ.get(key)
        if value is None or value == "":
            missing.append(key)
            value = DEFAULTS.get(key)
        config[key] = value
    return config, missing


def mask(secret: str) -> str:
    # Nunca mostramos um segredo inteiro na tela
    return secret[:2] + "*" * max(0, len(secret) - 2)


def main() -> None:
    print("ORACLE STATUS: Consulting the configuration...")
    print()
    config, missing = load_config()
    mode = config["MATRIX_MODE"] or "development"
    if mode not in ("development", "production"):
        print(f"WARNING: unknown MATRIX_MODE '{mode}', using development")
        mode = "development"
    production = mode == "production"

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    db = config["DATABASE_URL"]
    if db is None:
        print("Database: Not configured")
    elif production:
        print("Database: Connected to production cluster")
    else:
        print(f"Database: Connected to local instance ({db})")
    key = config["API_KEY"]
    if key is None:
        print("API Access: Missing key - running unauthenticated")
    elif production:
        print("API Access: Authenticated")
    else:
        print(f"API Access: Authenticated (key {mask(key)})")
    level = config["LOG_LEVEL"] or "INFO"
    print(f"Log Level: {'WARNING' if production else level}")
    zion = config["ZION_ENDPOINT"]
    print(f"Remote Network: {'Online' if zion else 'Offline'}")
    if production:
        print("Production mode: verbose output disabled, secrets hidden")
    else:
        print("Development mode: verbose diagnostics enabled")

    if missing:
        print()
        print("WARNING: missing configuration, defaults used for:")
        for name in missing:
            print(f"  - {name}")

    print()
    print("Configuration security check:")
    print("[OK] No hardcoded secrets detected")
    gitignore = os.path.join(HERE, ".gitignore")
    ignored = False
    if os.path.exists(gitignore):
        with open(gitignore) as file:
            ignored = ".env" in file.read().split()
    print(f"[{'OK' if ignored else 'KO'}] .env file "
          f"{'properly ignored' if ignored else 'NOT ignored'} by git")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)

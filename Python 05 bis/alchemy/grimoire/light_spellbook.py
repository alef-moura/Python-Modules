def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    # Import tardio (dentro da funcao): so acontece quando a funcao roda,
    # e nesse momento este modulo ja terminou de carregar. Sem ciclo!
    from .light_validator import validate_ingredients

    result = validate_ingredients(ingredients)
    if result.endswith("VALID") and not result.endswith("INVALID"):
        return f"Spell recorded: {spell_name} ({result})"
    return f"Spell rejected: {spell_name} ({result})"

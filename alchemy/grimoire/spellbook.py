def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    validity = validate_ingredients(ingredients)
    if " VALID" in validity:
        return f"Spell recorded: {spell_name} ({validity})"
    return f"Spell rejected: {spell_name} ({validity})"

def validate_ingredients(ingredients: str) -> str:
    """If the ingredients contain anything other than
    `fire`, `water`, `earth` or `air`, return:
    `[ingredients] - INVALID`, otherwise `[ingredients] - VALID`."""
    ingredients = ingredients.lower().split()
    for ingredient in ingredients:
        if "fire" in ingredient \
          or "water" in ingredient \
          or "earth" in ingredient \
          or "air" in ingredient:
            del ingredient
    if len(ingredients) > 0:
        return f"[{ingredients}] - INVALID"
    return f"[{ingredients}] - VALID"

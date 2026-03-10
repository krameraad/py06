def validate_ingredients(ingredients: str) -> str:
    """If the ingredients contain anything other than
    `fire`, `water`, `earth` or `air`, return:
    `[ingredients] - INVALID`, otherwise `[ingredients] - VALID`."""
    for ingredient in ingredients.lower().split():
        if ingredient not in ["fire", "water", "earth", "air"]:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"

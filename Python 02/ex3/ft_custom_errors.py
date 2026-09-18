class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")
    errors = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!"),
    ]
    for err in errors:
        try:
            raise err
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()

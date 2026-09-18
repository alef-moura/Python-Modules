class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


def water_plant(plant_name: str) -> None:
    if not plant_name.istitle():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for p in ["Tomato", "Lettuce", "Carrots"]:
            water_plant(p)
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    print("Opening watering system")
    try:
        for p in ["Tomato", "lettuce", "Carrots"]:
            water_plant(p)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("ending tests and returning to main")
    finally:
        print("Closing watering system")

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
        print()
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
        print()
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()

    for data in ["25", "abc", "100", "-50"]:
        print(f"Input data is '{data}'")
        try:
            temp = input_temperature(data)
            print(f"Temperature is now {temp}°C")
            print()
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
            print()

    print("All tests completed program didn't crash!")


if __name__ == "__main__":
    test_temperature()

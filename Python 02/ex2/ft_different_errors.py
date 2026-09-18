def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        _ = 1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        _ = "str" + 5  # type: ignore[operator]


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for op in range(5):
        print(f"Testing operation {op}...")
        try:
            garden_operations(op)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

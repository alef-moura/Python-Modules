class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, amount: float = 0.8) -> None:
        self.height += amount

    def age_plant(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25.0, 30)
    rose.show()

    initial_height = rose.height
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow(0.8)
        rose.age_plant()
        rose.show()

    growth = rose.height - initial_height
    print(f"Growth this week: {round(growth, 1)}cm")

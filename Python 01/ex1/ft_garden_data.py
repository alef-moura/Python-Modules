class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.0f}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    p1 = Plant("Rose", 25.0, 30)
    p2 = Plant("Sunflower", 80.0, 45)
    p3 = Plant("Cactus", 15.0, 120)

    p1.show()
    p2.show()
    p3.show()

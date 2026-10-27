#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    # Repete ate o usuario digitar coordenadas validas
    while True:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = raw.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        values: list[float] = []
        try:
            for part in parts:
                current = part.strip()
                values.append(float(current))
        except ValueError as error:
            print(f"Error on parameter '{current}': {error}")
            continue
        # Uma tupla e imutavel: depois de criada, nao muda mais
        return (values[0], values[1], values[2])


def distance(a: tuple[float, float, float],
             b: tuple[float, float, float]) -> float:
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
                     + (b[2] - a[2]) ** 2)


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first = get_player_pos()
    print(f"Got a first tuple: {first}")
    x, y, z = first  # desempacotamento da tupla
    print(f"It includes: X={x}, Y={y}, Z={z}")
    print(f"Distance to center: {round(distance((0, 0, 0), first), 4)}")
    print("Get a second set of coordinates")
    second = get_player_pos()
    print("Distance between the 2 sets of coordinates: "
          f"{round(distance(first, second), 4)}")


if __name__ == "__main__":
    main()

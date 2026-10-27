#!/usr/bin/env python3
import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    players = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory",
               "john", "kevin", "Liam"]
    print(f"Initial list of players: {players}")

    # Compreensao de lista: [expressao for item in lista if condicao]
    capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalized}")
    only_cap = [name for name in players if name == name.capitalize()]
    print(f"New list of capitalized names only: {only_cap}")

    # Compreensao de dicionario: {chave: valor for item in lista}
    scores = {name: random.randint(0, 1000) for name in capitalized}
    print(f"Score dict: {scores}")
    average = sum(scores.values()) / len(scores)
    print(f"Score average is {round(average, 2)}")
    high = {name: score for name, score in scores.items()
            if score > average}
    print(f"High scores: {high}")


if __name__ == "__main__":
    main()

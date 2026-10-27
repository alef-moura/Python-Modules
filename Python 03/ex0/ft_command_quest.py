#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Command Quest ===")
    # sys.argv e uma lista: posicao 0 = nome do programa, o resto = argumentos
    print(f"Program name: {sys.argv[0]}")
    args = sys.argv[1:]  # fatiamento (slice): tudo a partir do indice 1
    if len(args) == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args)}")
        index = 1
        for arg in args:
            print(f"Argument {index}: {arg}")
            index += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()

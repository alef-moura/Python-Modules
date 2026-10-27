#!/usr/bin/env python3
import random
import typing

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "eat", "sleep", "grab", "move", "climb", "swim",
           "use", "release"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    # Gerador infinito: cada next() produz UM evento, sob demanda
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(events: list[tuple[str, str]]
                  ) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randrange(len(events))
        yield events.pop(index)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    stream = gen_event()
    for i in range(1000):
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")

    events = [next(stream) for _ in range(10)]
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()

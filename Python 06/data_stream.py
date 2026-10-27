#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Interface comum: todo processador valida, ingere e devolve dados."""

    def __init__(self, name: str) -> None:
        self.name = name
        self._storage: list[tuple[int, str]] = []
        self._rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def _store(self, value: str) -> None:
        self._storage.append((self._rank, value))
        self._rank += 1

    def output(self) -> tuple[int, str]:
        # Fila (FIFO): o primeiro a entrar e o primeiro a sair
        if not self._storage:
            raise IndexError(f"{self.name}: no data to output")
        return self._storage.pop(0)

    def total(self) -> int:
        return self._rank

    def remaining(self) -> int:
        return len(self._storage)


def _is_number(value: Any) -> bool:
    # bool e subclasse de int em Python, por isso excluimos explicitamente
    return isinstance(value, (int, float)) and not isinstance(value, bool)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Numeric Processor")

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(_is_number(item) for item in data)
        return _is_number(data)

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._store(str(item))


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Text Processor")

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._store(item)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Log Processor")

    @staticmethod
    def _is_log(entry: Any) -> bool:
        return (isinstance(entry, dict)
                and all(isinstance(k, str) and isinstance(v, str)
                        for k, v in entry.items()))

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(self._is_log(item) for item in data)
        return self._is_log(data)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            level = item.get("log_level", "INFO")
            message = item.get("log_message", "")
            self._store(f"{level}: {message}")


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            # Polimorfismo: o stream nao sabe QUAL processador e,
            # so pergunta "voce aceita?" e chama ingest.
            for proc in self._processors:
                if proc.validate(element):
                    try:
                        proc.ingest(element)
                    except ValueError as error:
                        print(f"DataStream error - {error}")
                    break
            else:
                print("DataStream error - Can't process element in "
                      f"stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
        for proc in self._processors:
            print(f"{proc.name}: total {proc.total()} items processed, "
                  f"remaining {proc.remaining()} on processor")
        print()


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("Registering Numeric Processor\n")
    numeric = NumericProcessor()
    stream.register_processor(numeric)

    batch: list[Any] = [
        "Hello world", [3.14, -1, 2.71],
        [{"log_level": "WARNING",
          "log_message": "Telnet access! Use ssh instead"},
         {"log_level": "INFO", "log_message": "User wil is connected"}],
        42, ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch}\n")
    stream.process_stream(batch)
    print()
    stream.print_processors_stats()

    print("Registering other data processors")
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(text)
    stream.register_processor(log)
    print("Send the same batch again\n")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("Consume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for proc, count in ((numeric, 3), (text, 2), (log, 1)):
        for _ in range(count):
            proc.output()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()

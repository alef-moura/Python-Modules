#!/usr/bin/env python3
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from pydantic import BaseModel, Field, ValidationError

DATA_DIR = Path(__file__).resolve().parent.parent / "tools" / "generated_data"


class SpaceStation(BaseModel):
    """Cada campo declara o tipo e as restricoes; o Pydantic valida tudo."""

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)  # ge = >=, le = <=
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def show_station(station: SpaceStation) -> None:
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    status = "Operational" if station.is_operational else "Maintenance"
    print(f"Status: {status}")
    if station.notes:
        print(f"Notes: {station.notes}")


def load_json(name: str) -> list[dict[str, Any]]:
    try:
        with open(DATA_DIR / name) as file:
            data: list[dict[str, Any]] = json.load(file)
            return data
    except (OSError, json.JSONDecodeError):
        return []


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)
    # A string ISO e convertida automaticamente para datetime
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2024-01-15T10:30:00",  # type: ignore[arg-type]
    )
    print("Valid station created:")
    show_station(station)
    print("=" * 40)

    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="ISS002",
            name="Overcrowded Station",
            crew_size=25,
            power_level=50.0,
            oxygen_level=80.0,
            last_maintenance=datetime(2024, 1, 1),
        )
    except ValidationError as error:
        for detail in error.errors():
            print(detail["msg"])

    generated = load_json("space_stations.json")
    if generated:
        print("=" * 40)
        print(f"Validating {len(generated)} generated stations:")
        for raw in generated:
            # model_validate cria o modelo a partir de um dicionario
            item = SpaceStation.model_validate(raw)
            print(f"  [OK] {item.station_id}: {item.name}")

    invalid = load_json("invalid_stations.json")
    for raw in invalid:
        print("=" * 40)
        print(f"Invalid station '{raw.get('station_id')}':")
        try:
            SpaceStation.model_validate(raw)
        except ValidationError as error:
            for detail in error.errors():
                field = ".".join(str(part) for part in detail["loc"])
                print(f"  {field}: {detail['msg']}")


if __name__ == "__main__":
    main()

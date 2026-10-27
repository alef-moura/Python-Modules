#!/usr/bin/env python3
import json
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field, ValidationError, model_validator

DATA_DIR = Path(__file__).resolve().parent.parent / "tools" / "generated_data"


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    # Modelo aninhado: cada item da lista e validado como CrewMember
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_safety(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        leaders = [m for m in self.crew
                   if m.rank in (Rank.COMMANDER, Rank.CAPTAIN)]
        if not leaders:
            raise ValueError(
                "Mission must have at least one Commander or Captain")
        if self.duration_days > 365:
            experienced = [m for m in self.crew if m.years_experience >= 5]
            if len(experienced) * 2 < len(self.crew):
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced crew "
                    "(5+ years)")
        inactive = [m.name for m in self.crew if not m.is_active]
        if inactive:
            raise ValueError(
                f"All crew members must be active (inactive: "
                f"{', '.join(inactive)})")
        return self


def show_mission(mission: SpaceMission) -> None:
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value}) - "
              f"{member.specialization}")


def first_error(error: ValidationError) -> str:
    detail = error.errors()[0]
    msg = str(detail["msg"]).removeprefix("Value error, ")
    location = ".".join(str(part) for part in detail["loc"])
    return f"{location}: {msg}" if location else msg


def load_json(name: str) -> list[dict[str, Any]]:
    try:
        with open(DATA_DIR / name) as file:
            data: list[dict[str, Any]] = json.load(file)
            return data
    except (OSError, json.JSONDecodeError):
        return []


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 41)
    crew = [
        {"member_id": "CM001", "name": "Sarah Connor", "rank": "commander",
         "age": 45, "specialization": "Mission Command",
         "years_experience": 20},
        {"member_id": "CM002", "name": "John Smith", "rank": "lieutenant",
         "age": 35, "specialization": "Navigation", "years_experience": 10},
        {"member_id": "CM003", "name": "Alice Johnson", "rank": "officer",
         "age": 29, "specialization": "Engineering", "years_experience": 4},
    ]
    mission_data: dict[str, Any] = {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": "2024-06-01T09:00:00",
        "duration_days": 900,
        "crew": crew,
        "budget_millions": 2500.0,
    }
    mission = SpaceMission.model_validate(mission_data)
    print("Valid mission created:")
    show_mission(mission)

    no_leader = [dict(m, rank="officer") for m in crew]
    invalid_cases: list[dict[str, Any]] = [
        {"crew": no_leader},
        {"mission_id": "X2024_MARS"},
        {"crew": [dict(m, years_experience=1) for m in crew]},
        {"crew": crew[:2] + [dict(crew[2], is_active=False)]},
        # Erro dentro de um modelo aninhado (idade invalida)
        {"crew": crew[:2] + [dict(crew[2], age=12)]},
    ]
    for case in invalid_cases:
        print("=" * 41)
        print("Expected validation error:")
        try:
            SpaceMission.model_validate({**mission_data, **case})
        except ValidationError as error:
            print(first_error(error))

    generated = load_json("space_missions.json")
    if generated:
        print("=" * 41)
        print(f"Checking {len(generated)} generated missions:")
        for raw in generated:
            try:
                item = SpaceMission.model_validate(raw)
                print(f"  [OK] {item.mission_id}: {item.mission_name} "
                      f"({len(item.crew)} crew)")
            except ValidationError as error:
                print(f"  [KO] {raw.get('mission_id')}: {first_error(error)}")


if __name__ == "__main__":
    main()

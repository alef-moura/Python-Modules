#!/usr/bin/env python3
import json
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Optional

from pydantic import BaseModel, Field, ValidationError, model_validator

DATA_DIR = Path(__file__).resolve().parent.parent / "tools" / "generated_data"


class ContactType(str, Enum):
    """Enum: conjunto fechado de valores permitidos."""

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def check_business_rules(self) -> "AlienContact":
        # Roda DEPOIS da validacao dos campos: regras que envolvem varios
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if (self.contact_type == ContactType.PHYSICAL
                and not self.is_verified):
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")
        return self


def show_contact(contact: AlienContact) -> None:
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    if contact.message_received:
        print(f"Message: '{contact.message_received}'")


def first_error(error: ValidationError) -> str:
    msg = str(error.errors()[0]["msg"])
    # Mensagens de model_validator vem com o prefixo "Value error, "
    return msg.removeprefix("Value error, ")


def load_json(name: str) -> list[dict[str, Any]]:
    try:
        with open(DATA_DIR / name) as file:
            data: list[dict[str, Any]] = json.load(file)
            return data
    except (OSError, json.JSONDecodeError):
        return []


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 38)
    contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2024, 3, 14, 22, 30),
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
    )
    print("Valid contact report:")
    show_contact(contact)

    invalid_cases: list[dict[str, Any]] = [
        {"contact_id": "AC_2024_002", "contact_type": "telepathic",
         "witness_count": 1},
        {"contact_id": "XX_2024_003"},
        {"contact_id": "AC_2024_004", "contact_type": "physical",
         "is_verified": False},
        {"contact_id": "AC_2024_005", "signal_strength": 9.1,
         "message_received": None},
    ]
    base: dict[str, Any] = {
        "timestamp": "2024-05-01T03:00:00", "location": "Roswell",
        "contact_type": "visual", "signal_strength": 4.0,
        "duration_minutes": 20, "witness_count": 4,
    }
    for case in invalid_cases:
        print("=" * 38)
        print("Expected validation error:")
        try:
            AlienContact.model_validate({**base, **case})
        except ValidationError as error:
            print(first_error(error))

    generated = load_json("alien_contacts.json")
    if generated:
        print("=" * 38)
        print(f"Checking {len(generated)} generated contact reports:")
        for raw in generated:
            try:
                item = AlienContact.model_validate(raw)
                print(f"  [OK] {item.contact_id} ({item.contact_type.value})")
            except ValidationError as error:
                print(f"  [KO] {raw.get('contact_id')}: {first_error(error)}")


if __name__ == "__main__":
    main()

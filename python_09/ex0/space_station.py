from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=100)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)
    try:
        valid = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.fromisoformat("2026-07-27T12:00:00"),
            is_operational=True
        )
        print("Valid station created:")
        print(f"ID: {valid.station_id}")
        print(f"Name: {valid.name}")
        print(f"Crew: {valid.crew_size} people")
        print(f"Power: {valid.power_level}%")
        print(f"Oxygen: {valid.oxygen_level}%")
        print(f"Status: "
              f"{'Operationel' if valid.is_operational else 'Offline'}\n")
        print("=" * 40)
    except ValidationError as e:
        print("Expection validation error:", e)

    try:
        SpaceStation(
            station_id="IS",
            name="International Space Station",
            crew_size=25,
            power_level=99.0,
            oxygen_level=92.3,
            last_maintenance=datetime.now()
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"- {error['loc'][0]}: {error['msg']}")


if __name__ == "__main__":
    main()

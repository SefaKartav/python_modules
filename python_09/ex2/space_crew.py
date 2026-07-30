from enum import Enum
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(Enum):
    CADET = 'cadet'
    OFFICER = 'officer'
    LIEUTENANT = 'lieutenant'
    CAPTAIN = 'captain'
    COMMANDER = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation_rules(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        has_leader = False
        all_active = True
        experienced_count = 0

        for member in self.crew:
            if member.rank in [Rank.COMMANDER, Rank.CAPTAIN]:
                has_leader = True
            if not member.is_active:
                all_active = False
            if member.years_experience >= 5:
                experienced_count += 1

        if not has_leader:
            raise ValueError("Mission must have at "
                             "least one Commander or Captain")
        if not all_active:
            raise ValueError("All crew members must be active")
        if self.duration_days > 365:
            necessary = len(self.crew) / 2
            if necessary > experienced_count:
                raise ValueError("Long missions (> 365 days) need "
                                 "50% experienced crew (5+ years)")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 41)

    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Sarah ConnOr",
                    rank=Rank.COMMANDER,
                    age=45,
                    specialization="Mission Command",
                    years_experience=24
                ),
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=32,
                    specialization="Navigation",
                    years_experience=9
                ),
                CrewMember(
                    member_id="C003",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=28,
                    specialization="Engineering",
                    years_experience=4
                )
            ]
        )
        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for member in valid_mission.crew:
            print(f"- {member.name} ({member.rank.value}) "
                  f"- {member.specialization}")
        print("=" * 41)

    except ValidationError as e:
        print("Expected validation error:", e)

    try:
        SpaceMission(
            mission_id="M2024_MOON",
            mission_name="Moon Exploration",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=30,
            budget_millions=500.0,
            crew=[
                CrewMember(
                    member_id="C004",
                    name="Bob Builder",
                    rank=Rank.OFFICER,
                    age=30,
                    specialization="Construction",
                    years_experience=4
                )
            ]
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            clean_msg = error['msg'].replace("Value error, ", "")
            print(f"{clean_msg}")


if __name__ == "__main__":
    main()

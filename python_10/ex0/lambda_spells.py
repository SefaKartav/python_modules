from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda s: s["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda z: f"* {z} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    powers = list(map(lambda m: m["power"], mages))
    maxx = max(powers, key=lambda f: f)
    minn = min(powers, key=lambda f: f)
    avgg = round(sum(powers) / len(powers), 2)

    return {"max_power": maxx, "min_power": minn, "avg_power": avgg}


if __name__ == "__main__":
    print("Testing artifact sorter...")
    sample_artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "relieq"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"}
    ]
    sorted_arts = artifact_sorter(sample_artifacts)
    print(f"{sorted_arts[0]['name']} "
          f"({sorted_arts[0]['power']} "
          f"power) comes before {sorted_arts[1]['name']} "
          f"({sorted_arts[1]['power']} power)")

    print("\nTesting spell transformer...")
    sample_spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(sample_spells)
    print(" ".join(transformed))

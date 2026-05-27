import random

ALL_ACHIEVEMENTS: list[str] = [
    "First Steps", "Speed Runner", "Survivor", "Master Explorer",
    "Treasure Hunter", "Boss Slayer", "Crafting Genius", "World Savior",
    "Untouchable", "Unstoppable", "Strategist", "Collector Supreme",
    "Sharp Mind", "Hidden Path Finder", "Night Owl", "Dragon Slayer",
    "Pacifist", "Speedster", "Legend", "Ghost",
]

PLAYERS: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]


def gen_player_achievements() -> set[str]:
    count: int = random.randint(4, 10)
    picked: list[str] = random.sample(ALL_ACHIEVEMENTS, count)
    return set(picked)


def main() -> None:
    print("=== Achievement Tracker System ===")

    player_achievements: dict[str, set[str]] = {
        name: gen_player_achievements() for name in PLAYERS
    }

    for name, achievements in player_achievements.items():
        print(f"Player {name}: {achievements}")

    all_distinct: set[str] = set()

    for achievements in player_achievements.values():
        all_distinct = all_distinct.union(achievements)

    print(f"All distinct achievements: {all_distinct}")

    common: set[str] = set()
    first: bool = True

    for achievements in player_achievements.values():
        if first:
            common = achievements
            first = False
        else:
            common = common.intersection(achievements)

    print(f"Common achievements: {common}")

    for name, achievements in player_achievements.items():
        others: set[str] = set()

        for other_name, other_achievements in (
            player_achievements.items()
        ):
            if other_name != name:
                others = others.union(other_achievements)

        exclusive: set[str] = achievements.difference(others)
        print(f"Only {name} has: {exclusive}")

    for name, achievements in player_achievements.items():
        missing: set[str] = all_distinct.difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()

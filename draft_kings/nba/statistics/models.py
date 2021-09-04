from dataclasses import dataclass


@dataclass(init=True,
           repr=True,
           eq=True,
           order=False,
           unsafe_hash=False,
           frozen=True)
class Statistics:
    points_scored: int
    three_pointers_made: int
    assists: int
    rebounds: int
    steals: int
    blocks: int
    turnovers: int

    def __post_init__(self):
        if self.points_scored < 3 * self.three_pointers_made:
            raise ValueError(
                "Points scored is contradicted by three-pointers made")

        if 0 > self.points_scored:
            raise ValueError("Points scored cannot be negative")

        if 0 > self.three_pointers_made:
            raise ValueError("Three-pointers made cannot be negative")

        if 0 > self.assists:
            raise ValueError("Assists cannot be negative")

        if 0 > self.rebounds:
            raise ValueError("Rebounds cannot be negative")

        if 0 > self.steals:
            raise ValueError("Steals cannot be negative")

        if 0 > self.blocks:
            raise ValueError("Blocks cannot be negative")

        if 0 > self.turnovers:
            raise ValueError("Turnovers cannot be negative")

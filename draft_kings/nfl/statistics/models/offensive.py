from dataclasses import dataclass


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=True)
class YardageStatistics:
    passing: int
    rushing: int
    receiving: int


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=True)
class KickReturnTouchdownStatistics:
    punts: int
    kickoffs: int
    field_goals: int

    def __post_init__(self):
        if 0 > self.punts or 0 > self.kickoffs or 0 > self.field_goals:
            raise ValueError("touchdowns cannot be negative")


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=True)
class TouchdownStatistics:
    passing: int
    rushing: int
    receiving: int
    kick_returns: KickReturnTouchdownStatistics
    fumble_recoveries: int

    def __post_init__(self):
        if 0 > self.passing or 0 > self.rushing or 0 > self.receiving or 0 > self.fumble_recoveries:
            raise ValueError("touchdowns cannot be negative")


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=True)
class TwoPointConversionStatistics:
    thrown: int
    rushed: int
    caught: int

    def __post_init__(self):
        if 0 > self.thrown or 0 > self.rushed or 0 > self.caught:
            raise ValueError("conversions cannot be negative")


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=True)
class ConversionStatistics:
    two_point: TwoPointConversionStatistics


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=True)
class ScoringStatistics:
    touchdowns: TouchdownStatistics
    conversions: ConversionStatistics


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=True)
class TurnoverStatistics:
    interceptions: int
    fumbles_lost: int

    def __post_init__(self):
        if 0 > self.interceptions or 0 > self.fumbles_lost:
            raise ValueError("turnovers cannot be negative")


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=True)
class OffensiveStatistics:
    yards: YardageStatistics
    scoring: ScoringStatistics
    turnovers: TurnoverStatistics
    receptions: int

    def __post_init__(self):
        if 0 > self.receptions:
            raise ValueError("receptions cannot be negative")

from dataclasses import dataclass
from enum import Enum

from .offensive import KickReturnTouchdownStatistics

"""
From https://www.draftkings.com/help/rules/1/1:
"The following scoring plays will result in Points Allowed by your Defense/Special Teams:
Rushing TDs, Passing TDs, Offensive Fumble Recovery TDs, Punt Return TDs, Kick Return TDs, FG Return TDs, Blocked FG TDs, Blocked Punt TDs
2pt conversions
2 Point Conversion/Extra-point Returns
Extra-points
Field-goals"
"""


class PointsAllowed(Enum):
    _0 = "0 Points Allowed"
    _1_TO_6 = "1 – 6 Points Allowed"
    _7_TO_13 = "7 – 13 Points Allowed"
    _14_TO_20 = "14 – 20 Points Allowed"
    _21_TO_27 = "21 – 27 Points Allowed"
    _28_TO_24 = "28 – 34 Points Allowed"
    _35_OR_MORE = "35+ Points Allowed"


@dataclass(init=True,
           repr=True,
           eq=True,
           order=False,
           unsafe_hash=False,
           frozen=True)
class BlockedKickReturnTouchdownStatistics:
    punts: int
    field_goals: int

    def __post_init__(self):
        if 0 > self.punts or 0 > self.field_goals:
            raise ValueError(
                "blocked punt or field goals returned for touchdowns cannot be negative")


@dataclass(init=True,
           repr=True,
           eq=True,
           order=False,
           unsafe_hash=False,
           frozen=True)
class TurnoverReturnTouchdownStatistics:
    interceptions: int
    fumble_recoveries: int

    def __post_init__(self):
        if 0 > self.interceptions or 0 > self.fumble_recoveries:
            raise ValueError("touchdowns cannot be negative")


@dataclass(init=True,
           repr=True,
           eq=True,
           order=False,
           unsafe_hash=False,
           frozen=True)
class TouchdownStatistics:
    kick_returns: KickReturnTouchdownStatistics
    blocked_kicks: BlockedKickReturnTouchdownStatistics
    turnovers: TurnoverReturnTouchdownStatistics


@dataclass(init=True,
           repr=True,
           eq=True,
           order=False,
           unsafe_hash=False,
           frozen=True)
class ScoringStatistics:
    touchdowns: TouchdownStatistics
    safeties: int
    conversion_returns: int

    def __post_init__(self):
        if 0 > self.safeties:
            raise ValueError("safeties cannot be negative")

        if 0 > self.conversion_returns:
            raise ValueError("conversion returns cannot be negative")


@dataclass(init=True,
           repr=True,
           eq=True,
           order=False,
           unsafe_hash=False,
           frozen=True)
class TurnoverStatistics:
    interceptions: int
    fumble_recoveries: int

    def __post_init__(self):
        if 0 > self.interceptions:
            raise ValueError("interceptions cannot be negative")

        if 0 > self.fumble_recoveries:
            raise ValueError("fumble recoveries cannot be negative")


@dataclass(init=True,
           repr=True,
           eq=True,
           order=False,
           unsafe_hash=False,
           frozen=True)
class DefensiveStatistics:
    scoring: ScoringStatistics
    turnovers: TurnoverStatistics
    sacks: int
    # blocked kicks are not considered turnovers since "a turnover occurs when the team with the ball loses
    # possession of the ball without kicking it, which is then gained by the other team. In American football,
    # the two events that are officially classified as "turnovers" are fumbles (accidental loss of a live ball after
    # a player has possession)[1] and interceptions (passes intended for a member of the passing team, but caught by
    # a member of the defending team)."
    # https://en.wikipedia.org/wiki/Turnover_(gridiron_football)
    blocked_kicks: int
    points_allowed: PointsAllowed

    def __post_init__(self):
        if 0 > self.sacks:
            raise ValueError("sacks cannot be negative")

        if 0 > self.blocked_kicks:
            raise ValueError("blocked kicks cannot be negative")

        if self.blocked_kicks < (
                self.scoring.touchdowns.blocked_kicks.field_goals +
                self.scoring.touchdowns.blocked_kicks.punts):
            raise ValueError(
                "blocked kicks must be greater than or equal to the number of blocked field goals or punts returned "
                "for a touchdown")

        if self.turnovers.fumble_recoveries < self.scoring.touchdowns.turnovers.fumble_recoveries:
            raise ValueError(
                "fumble recoveries must be greater than or equal to the number of fumble recovery touchdowns"
            )

        if self.turnovers.interceptions < self.scoring.touchdowns.turnovers.interceptions:
            raise ValueError(
                "interceptions must be greater than or equal to the number of interceptions returned for a touchdown"
            )

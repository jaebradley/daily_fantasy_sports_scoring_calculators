from unittest import TestCase

from daily_fantasy_sports_scoring_calculators.draft_kings.nfl.statistics.models.defensive \
    import BlockedKickReturnTouchdownStatistics, TurnoverReturnTouchdownStatistics, TouchdownStatistics, \
    ScoringStatistics, TurnoverStatistics, DefensiveStatistics, PointsAllowed
from daily_fantasy_sports_scoring_calculators.draft_kings.nfl.statistics.models.offensive \
    import KickReturnTouchdownStatistics


class TestBlockedKickReturnTouchdownStatistics(TestCase):
    def test_negative_points_and_field_goals(self):
        with self.assertRaises(ValueError):
            BlockedKickReturnTouchdownStatistics(
                punts=-1,
                field_goals=-1
            )

    def test_negative_points_and_zero_field_goals(self):
        with self.assertRaises(ValueError):
            BlockedKickReturnTouchdownStatistics(
                punts=-1,
                field_goals=0
            )

    def test_zero_points_and_negative_field_goals(self):
        with self.assertRaises(ValueError):
            BlockedKickReturnTouchdownStatistics(
                punts=0,
                field_goals=-1
            )

    def test_zero_points_and_zero_field_goals(self):
        for punts in range(0, 2):
            for field_goals in range(0, 2):
                try:
                    BlockedKickReturnTouchdownStatistics(
                        punts=punts, field_goals=field_goals)
                except ValueError:
                    self.fail("expected object creation to succeed")


class TestTurnoverReturnTouchdownStatistics(TestCase):
    def test_invalid_values(self):
        for interceptions in range(-1, 1):
            for fumble_recoveries in range(-1, 1):
                if 0 != interceptions and 0 != fumble_recoveries:
                    try:
                        TurnoverReturnTouchdownStatistics(
                            interceptions=interceptions, fumble_recoveries=fumble_recoveries)
                        self.fail("expected object creation to fail")
                    except ValueError:
                        continue

    def test_valid_values(self):
        for interceptions in range(0, 2):
            for fumble_recoveries in range(0, 2):
                try:
                    TurnoverReturnTouchdownStatistics(
                        interceptions=interceptions, fumble_recoveries=fumble_recoveries)
                except ValueError:
                    self.fail("expected object creation to succeed")


class TestScoringStatistics(TestCase):
    def setUp(self) -> None:
        self.touchdowns = TouchdownStatistics(
            kick_returns=KickReturnTouchdownStatistics(
                punts=0,
                kickoffs=0,
                field_goals=0),
            blocked_kicks=BlockedKickReturnTouchdownStatistics(
                punts=0,
                field_goals=0),
            turnovers=TurnoverReturnTouchdownStatistics(
                interceptions=0,
                fumble_recoveries=0))

    def test_invalid_values(self):
        for safeties in range(-1, 1):
            for conversion_returns in range(-1, 1):
                if 0 != safeties and 0 != conversion_returns:
                    try:
                        ScoringStatistics(
                            touchdowns=self.touchdowns,
                            safeties=safeties,
                            conversion_returns=conversion_returns)
                        self.fail("expected object creation to fail")
                    except ValueError:
                        continue

    def test_valid_values(self):
        for safeties in range(0, 2):
            for conversion_returns in range(0, 2):
                try:
                    ScoringStatistics(
                        touchdowns=self.touchdowns,
                        safeties=safeties,
                        conversion_returns=conversion_returns)
                except ValueError:
                    self.fail("expected object creation to succeed")


class TestTurnoverStatistics(TestCase):
    def test_invalid_values(self):
        for interceptions in range(-1, 1):
            for fumble_recoveries in range(-1, 1):
                if 0 != interceptions and 0 != fumble_recoveries:
                    try:
                        TurnoverStatistics(
                            interceptions=interceptions,
                            fumble_recoveries=fumble_recoveries)
                        self.fail("expected object creation to fail")
                    except ValueError:
                        continue

    def test_valid_values(self):
        for interceptions in range(0, 2):
            for fumble_recoveries in range(0, 2):
                try:
                    TurnoverStatistics(
                        interceptions=interceptions,
                        fumble_recoveries=fumble_recoveries)
                except ValueError:
                    self.fail("expected object creation to succeed")


class TestDefensiveStatistics(TestCase):
    def test_invalid_sacks(self):
        with self.assertRaises(ValueError):
            DefensiveStatistics(
                scoring=ScoringStatistics(
                    touchdowns=TouchdownStatistics(
                        kick_returns=KickReturnTouchdownStatistics(
                            punts=0,
                            kickoffs=0,
                            field_goals=0),
                        blocked_kicks=BlockedKickReturnTouchdownStatistics(
                            punts=0,
                            field_goals=0),
                        turnovers=TurnoverReturnTouchdownStatistics(
                            interceptions=0,
                            fumble_recoveries=0)),
                    safeties=0,
                    conversion_returns=0),
                turnovers=TurnoverStatistics(
                    interceptions=0,
                    fumble_recoveries=0),
                sacks=-1,
                blocked_kicks=0,
                points_allowed=PointsAllowed._0)

    def test_invalid_blocked_kicks(self):
        with self.assertRaises(ValueError):
            DefensiveStatistics(
                scoring=ScoringStatistics(
                    touchdowns=TouchdownStatistics(
                        kick_returns=KickReturnTouchdownStatistics(
                            punts=0,
                            kickoffs=0,
                            field_goals=0),
                        blocked_kicks=BlockedKickReturnTouchdownStatistics(
                            punts=0,
                            field_goals=0),
                        turnovers=TurnoverReturnTouchdownStatistics(
                            interceptions=0,
                            fumble_recoveries=0)),
                    safeties=0,
                    conversion_returns=0),
                turnovers=TurnoverStatistics(
                    interceptions=0,
                    fumble_recoveries=0),
                sacks=0,
                blocked_kicks=-1,
                points_allowed=PointsAllowed._0)

        with self.assertRaises(ValueError):
            DefensiveStatistics(
                scoring=ScoringStatistics(
                    touchdowns=TouchdownStatistics(
                        kick_returns=KickReturnTouchdownStatistics(
                            punts=0,
                            kickoffs=0,
                            field_goals=0),
                        blocked_kicks=BlockedKickReturnTouchdownStatistics(
                            punts=1,
                            field_goals=0),
                        turnovers=TurnoverReturnTouchdownStatistics(
                            interceptions=0,
                            fumble_recoveries=0)),
                    safeties=0,
                    conversion_returns=0),
                turnovers=TurnoverStatistics(
                    interceptions=0,
                    fumble_recoveries=0),
                sacks=0,
                blocked_kicks=0,
                points_allowed=PointsAllowed._0)

        with self.assertRaises(ValueError):
            DefensiveStatistics(
                scoring=ScoringStatistics(
                    touchdowns=TouchdownStatistics(
                        kick_returns=KickReturnTouchdownStatistics(
                            punts=0,
                            kickoffs=0,
                            field_goals=0),
                        blocked_kicks=BlockedKickReturnTouchdownStatistics(
                            punts=0,
                            field_goals=1),
                        turnovers=TurnoverReturnTouchdownStatistics(
                            interceptions=0,
                            fumble_recoveries=0)),
                    safeties=0,
                    conversion_returns=0),
                turnovers=TurnoverStatistics(
                    interceptions=0,
                    fumble_recoveries=0),
                sacks=0,
                blocked_kicks=0,
                points_allowed=PointsAllowed._0)

    def test_invalid_turnovers(self):
        with self.assertRaises(ValueError):
            DefensiveStatistics(
                scoring=ScoringStatistics(
                    touchdowns=TouchdownStatistics(
                        kick_returns=KickReturnTouchdownStatistics(
                            punts=0,
                            kickoffs=0,
                            field_goals=0),
                        blocked_kicks=BlockedKickReturnTouchdownStatistics(
                            punts=0,
                            field_goals=0),
                        turnovers=TurnoverReturnTouchdownStatistics(
                            interceptions=1,
                            fumble_recoveries=0)),
                    safeties=0,
                    conversion_returns=0),
                turnovers=TurnoverStatistics(
                    interceptions=0,
                    fumble_recoveries=0),
                sacks=0,
                blocked_kicks=0,
                points_allowed=PointsAllowed._0)

        with self.assertRaises(ValueError):
            DefensiveStatistics(
                scoring=ScoringStatistics(
                    touchdowns=TouchdownStatistics(
                        kick_returns=KickReturnTouchdownStatistics(
                            punts=0,
                            kickoffs=0,
                            field_goals=0),
                        blocked_kicks=BlockedKickReturnTouchdownStatistics(
                            punts=0,
                            field_goals=0),
                        turnovers=TurnoverReturnTouchdownStatistics(
                            interceptions=0,
                            fumble_recoveries=1)),
                    safeties=0,
                    conversion_returns=0),
                turnovers=TurnoverStatistics(
                    interceptions=0,
                    fumble_recoveries=0),
                sacks=0,
                blocked_kicks=0,
                points_allowed=PointsAllowed._0)

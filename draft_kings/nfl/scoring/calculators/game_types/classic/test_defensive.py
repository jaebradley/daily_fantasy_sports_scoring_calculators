from unittest import TestCase

from draft_kings.nfl.scoring.calculators.game_types.classic.defensive import points_calculator
from draft_kings.nfl.statistics.models.defensive import BlockedKickReturnTouchdownStatistics, \
    TurnoverReturnTouchdownStatistics, TouchdownStatistics, \
    ScoringStatistics, TurnoverStatistics, DefensiveStatistics, PointsAllowed
from draft_kings.nfl.statistics.models.offensive import KickReturnTouchdownStatistics


class TestPointsCalculator(TestCase):
    def test_zero_points(self):
        self.assertEqual(
            0,
            points_calculator.calculate_points(
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
                    blocked_kicks=0,
                    points_allowed=PointsAllowed._21_TO_27)))

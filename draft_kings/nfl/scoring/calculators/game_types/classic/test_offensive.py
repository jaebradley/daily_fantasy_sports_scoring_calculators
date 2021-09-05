from unittest import TestCase

from draft_kings.nfl.scoring.calculators.game_types.classic.offensive import points_calculator
from draft_kings.nfl.statistics.models.offensive import OffensiveStatistics, \
    ScoringStatistics, TurnoverStatistics, TouchdownStatistics, YardageStatistics, \
    KickReturnTouchdownStatistics, ConversionStatistics, TwoPointConversionStatistics


class TestPointsCalculator(TestCase):
    def test_single_passing_touchdown(self):
        self.assertEqual(
            4,
            points_calculator.calculate_points(
                value=OffensiveStatistics(
                    yards=YardageStatistics(
                        passing=0,
                        rushing=0,
                        receiving=0
                    ),
                    scoring=ScoringStatistics(
                        touchdowns=TouchdownStatistics(
                            passing=1,
                            rushing=0,
                            receiving=0,
                            kick_returns=KickReturnTouchdownStatistics(
                                kickoffs=0,
                                punts=0,
                                field_goals=0
                            ),
                            fumble_recoveries=0
                        ),
                        conversions=ConversionStatistics(
                            two_point=TwoPointConversionStatistics(
                                caught=0,
                                thrown=0,
                                rushed=0
                            )
                        )
                    ),
                    turnovers=TurnoverStatistics(
                        interceptions=0,
                        fumbles_lost=0
                    ),
                    receptions=0
                )
            )
        )

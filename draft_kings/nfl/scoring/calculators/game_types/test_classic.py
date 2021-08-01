from unittest import TestCase
from draft_kings.nfl.scoring.calculators.game_types.classic import points_calculator
from draft_kings.nfl.statistics.models.offensive import OffensiveStatistics, ScoringStatistics, TurnoverStatistics, \
    TouchdownStatistics, YardageStatistics


class TestPointsCalculator(TestCase):
    def test_single_passing_touchdown(self):
        self.assertEqual(
            4,
            points_calculator.calculate_points(
                OffensiveStatistics(
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
                            kick_returns=0,
                            fumble_recoveries=0
                        ),
                        two_point_conversions=0
                    ),
                    turnovers=TurnoverStatistics(
                        interceptions=0,
                        fumbles_lost=0
                    ),
                    receptions=0
                )
            )
        )

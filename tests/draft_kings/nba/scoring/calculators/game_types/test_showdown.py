from unittest import TestCase

from daily_fantasy_sports_scoring_calculators.draft_kings.nba.scoring.calculators.game_types.showdown import \
    points_calculator
from daily_fantasy_sports_scoring_calculators.draft_kings.nba.statistics.models import Statistics


class TestPointsCalculator(TestCase):
    def test_zero(self):
        self.assertEqual(
            0,
            points_calculator.calculate_points(
                Statistics(
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                ),
                False
            )
        )
        self.assertEqual(
            0,
            points_calculator.calculate_points(
                Statistics(
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                ),
                True
            )
        )

    def test_points_scored(self):
        self.assertEqual(
            1,
            points_calculator.calculate_points(
                Statistics(
                    1,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                ),
                False
            )
        )
        self.assertEqual(
            1.5,
            points_calculator.calculate_points(
                Statistics(
                    1,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                ),
                True
            )
        )

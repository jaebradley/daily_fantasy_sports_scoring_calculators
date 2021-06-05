from unittest import TestCase
from draft_kings.nba.classic.calculators.scoring import points_calculator
from draft_kings.nba.classic.calculators.scoring.calculators import ClassicStatistics


class TestPointsCalculator(TestCase):
    def test_zero(self):
        self.assertEqual(
            0,
            points_calculator.calculate_points(
                ClassicStatistics(
                    points_scored=0,
                    three_pointers_made=0,
                    assists=0,
                    rebounds=0,
                    steals=0,
                    blocks=0,
                    turnovers=0
                )
            )
        )

    def test_negative(self):
        self.assertEqual(
            -0.5,
            points_calculator.calculate_points(
                ClassicStatistics(
                    points_scored=0,
                    three_pointers_made=0,
                    assists=0,
                    rebounds=0,
                    steals=0,
                    blocks=0,
                    turnovers=1
                )
            )
        )

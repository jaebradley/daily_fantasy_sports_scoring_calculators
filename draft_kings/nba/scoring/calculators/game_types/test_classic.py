from unittest import TestCase

from draft_kings.nba.scoring.calculators.game_types.classic import points_calculator
from draft_kings.nba.statistics.models import Statistics


class TestPointsCalculator(TestCase):
    def test_zero(self):
        self.assertEqual(
            0,
            points_calculator.calculate_points(
                Statistics(
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
                Statistics(
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

    def test_three_pointers_made(self):
        self.assertEqual(
            3.5,
            points_calculator.calculate_points(
                Statistics(
                    points_scored=3,
                    three_pointers_made=1,
                    assists=0,
                    rebounds=0,
                    steals=0,
                    blocks=0,
                    turnovers=0
                )
            )
        )

    def test_double_double(self):
        self.assertEqual(
            26.5,
            points_calculator.calculate_points(
                Statistics(
                    points_scored=10,
                    three_pointers_made=0,
                    assists=10,
                    rebounds=0,
                    steals=0,
                    blocks=0,
                    turnovers=0
                )
            )
        )

    def test_triple_double(self):
        self.assertEqual(
            42,
            points_calculator.calculate_points(
                Statistics(
                    points_scored=10,
                    three_pointers_made=0,
                    assists=10,
                    rebounds=10,
                    steals=0,
                    blocks=0,
                    turnovers=0
                )
            )
        )

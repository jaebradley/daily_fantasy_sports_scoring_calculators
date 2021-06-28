from unittest import TestCase

from .showdown import points_calculator
from draft_kings.nba.statistics import Statistics


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

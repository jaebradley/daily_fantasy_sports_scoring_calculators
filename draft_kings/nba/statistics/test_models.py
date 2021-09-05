from unittest import TestCase

from draft_kings.nba.statistics.models import Statistics


class TestStatistics(TestCase):
    def test_three_pointers_made_points_scored_validation(self):
        with self.assertRaises(ValueError) as error:
            Statistics(
                points_scored=0,
                three_pointers_made=1,
                assists=0,
                rebounds=0,
                steals=0,
                blocks=0,
                turnovers=0
            )

        self.assertEqual(
            "Points scored is contradicted by three-pointers made",
            str(error.exception)
        )

    def test_equality(self):
        self.assertEqual(
            Statistics(
                points_scored=0,
                three_pointers_made=0,
                assists=0,
                rebounds=0,
                steals=0,
                blocks=0,
                turnovers=0
            ),
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

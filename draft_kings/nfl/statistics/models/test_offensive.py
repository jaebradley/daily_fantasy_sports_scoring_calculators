from unittest import TestCase

from draft_kings.nfl.statistics.models.offensive import KickReturnTouchdownStatistics, TouchdownStatistics, \
    TwoPointConversionStatistics, TurnoverStatistics, OffensiveStatistics, YardageStatistics, ScoringStatistics, ConversionStatistics


class TestKickReturnTouchdownStatistics(TestCase):
    def test_invalid_kick_return_touchdown_statistics(self):
        with self.assertRaises(ValueError):
            KickReturnTouchdownStatistics(
                punts=-1,
                kickoffs=0,
                field_goals=0
            )

        with self.assertRaises(ValueError):
            KickReturnTouchdownStatistics(
                punts=0,
                kickoffs=-1,
                field_goals=0
            )

        with self.assertRaises(ValueError):
            KickReturnTouchdownStatistics(
                punts=0,
                kickoffs=0,
                field_goals=-1
            )

    def test_valid_kick_return_touchdown_statistics(self):
        max_value = 2

        for punts in range(max_value):
            for kickoffs in range(max_value):
                for field_goals in range(max_value):
                    stats = KickReturnTouchdownStatistics(
                        punts=punts, kickoffs=kickoffs, field_goals=field_goals)
                    self.assertEqual(punts, stats.punts)
                    self.assertEqual(kickoffs, stats.kickoffs)
                    self.assertEqual(field_goals, stats.field_goals)

    def test_invalid_touchdown_statistics(self):
        kick_return_statistics = KickReturnTouchdownStatistics(
            punts=0, kickoffs=0, field_goals=0)

        with self.assertRaises(ValueError):
            TouchdownStatistics(
                passing=-1,
                rushing=0,
                receiving=0,
                kick_returns=kick_return_statistics,
                fumble_recoveries=0
            )

        with self.assertRaises(ValueError):
            TouchdownStatistics(
                passing=0,
                rushing=-1,
                receiving=0,
                kick_returns=kick_return_statistics,
                fumble_recoveries=0
            )

        with self.assertRaises(ValueError):
            TouchdownStatistics(
                passing=0,
                rushing=0,
                receiving=-1,
                kick_returns=kick_return_statistics,
                fumble_recoveries=0
            )

        with self.assertRaises(ValueError):
            TouchdownStatistics(
                passing=0,
                rushing=0,
                receiving=0,
                kick_returns=kick_return_statistics,
                fumble_recoveries=-1
            )

    def test_valid_touchdown_statistics(self):
        kick_return_statistics = KickReturnTouchdownStatistics(
            punts=0, kickoffs=0, field_goals=0)
        max_value = 2

        for passing in range(max_value):
            for rushing in range(max_value):
                for receiving in range(max_value):
                    for fumble_recoveries in range(max_value):
                        stats = TouchdownStatistics(
                            passing=passing,
                            rushing=rushing,
                            receiving=receiving,
                            kick_returns=kick_return_statistics,
                            fumble_recoveries=fumble_recoveries
                        )
                        self.assertEqual(passing, stats.passing)
                        self.assertEqual(rushing, stats.rushing)
                        self.assertEqual(receiving, stats.receiving)
                        self.assertEqual(
                            fumble_recoveries, stats.fumble_recoveries)

    def test_invalid_two_point_conversion_statistics(self):
        with self.assertRaises(ValueError):
            TwoPointConversionStatistics(
                thrown=-1,
                rushed=0,
                caught=0
            )

        with self.assertRaises(ValueError):
            TwoPointConversionStatistics(
                thrown=0,
                rushed=-1,
                caught=0
            )

        with self.assertRaises(ValueError):
            TwoPointConversionStatistics(
                thrown=0,
                rushed=0,
                caught=-1
            )

    def test_valid_two_point_conversion_statistics(self):
        max_value = 2

        for thrown in range(max_value):
            for rushed in range(max_value):
                for caught in range(max_value):
                    stats = TwoPointConversionStatistics(
                        thrown=thrown,
                        rushed=rushed,
                        caught=caught
                    )

                    self.assertEqual(thrown, stats.thrown)
                    self.assertEqual(rushed, stats.rushed)
                    self.assertEqual(caught, stats.caught)

    def test_invalid_turnover_statistics(self):
        with self.assertRaises(ValueError):
            TurnoverStatistics(interceptions=-1, fumbles_lost=0)

        with self.assertRaises(ValueError):
            TurnoverStatistics(interceptions=0, fumbles_lost=-1)

    def test_valid_turnover_statistics(self):
        max_value = 2

        for interceptions in range(max_value):
            for fumbles_lost in range(max_value):
                statistics = TurnoverStatistics(
                    interceptions=interceptions, fumbles_lost=fumbles_lost)

                self.assertEqual(interceptions, statistics.interceptions)
                self.assertEqual(fumbles_lost, statistics.fumbles_lost)

    def test_invalid_offensive_statistics(self):
        with self.assertRaises(ValueError):
            OffensiveStatistics(
                yards=YardageStatistics(
                    passing=0,
                    rushing=0,
                    receiving=0
                ),
                scoring=ScoringStatistics(
                    touchdowns=TouchdownStatistics(
                        passing=0,
                        rushing=0,
                        receiving=0,
                        kick_returns=KickReturnTouchdownStatistics(
                            punts=0,
                            kickoffs=0,
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
                receptions=-1
            )

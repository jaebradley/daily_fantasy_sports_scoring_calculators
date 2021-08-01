from draft_kings.nfl.statistics.models.offensive import OffensiveStatistics
from shared.calculators.scoring import StatisticalValueCalculator


class PassingTouchdownsValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.scoring.touchdown.passing


class PassingYardageValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.yards.passing


class YardageLimitReachedCalculator(StatisticalValueCalculator):
    def __init__(self, yardage_value_calculator: StatisticalValueCalculator, inclusive_yardage_limit: int) -> None:
        super().__init__()
        self.yardage_value_calculator = yardage_value_calculator
        self.inclusive_yardage_limit = inclusive_yardage_limit

    def calculate_value(self, statistics: OffensiveStatistics):
        return self.inclusive_yardage_limit >= self.yardage_value_calculator.calculate_value(statistics)


class InterceptionsValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.turnovers.interceptions


class RushingTouchdownsValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.scoring.touchdown.rushing


class RushingYardageValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.yards.rushing


class ReceivingTouchdownsValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.scoring.touchdown.receiving


class ReceptionsValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.receptions


class ReceivingYardageValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.yards.receiving


class KickoffsReturnTouchdownsValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.scoring.touchdown.kick_returns.kickoffs


class PuntReturnTouchdownsValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.scoring.touchdown.kick_returns.punts


class FieldGoalReturnTouchdownsValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.scoring.touchdown.kick_returns.field_goals


class FumblesLostValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.turnovers.fumbles_lost


class TwoPointConversionsCaughtValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.scoring.conversions.two_point.caught


class TwoPointConversionsRushedValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.scoring.conversions.two_point.rushed


class TwoPointConversionsThrownValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.scoring.conversions.two_point.thrown


class FumbleRecoveryTouchdownsValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.scoring.touchdowns.fumble_recoveries


passing_touchdowns_value_calculator = PassingTouchdownsValueCalculator()
passing_yardage_value_calculator = PassingYardageValueCalculator()
at_least_300_yards_passing_value_calculator = YardageLimitReachedCalculator(
    yardage_value_calculator=passing_yardage_value_calculator,
    inclusive_yardage_limit=300
)
at_least_100_yards_rushing_calculator = YardageLimitReachedCalculator(
    yardage_value_calculator=RushingYardageValueCalculator(),
    inclusive_yardage_limit=100
)
at_least_100_yards_receiving_calculator = YardageLimitReachedCalculator(
    yardage_value_calculator=ReceivingYardageValueCalculator(),
    inclusive_yardage_limit=100
)
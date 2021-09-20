from daily_fantasy_sports_scoring_calculators.draft_kings.nfl.statistics.models.offensive import OffensiveStatistics
from daily_fantasy_sports_scoring_calculators.core.calculators.scoring import StatisticalValueCalculator


class PassingTouchdownsCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.scoring.touchdowns.passing


class PassingYardageCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.yards.passing


class HasAchievedMinimumYardageRequirementCalculator(StatisticalValueCalculator):
    def __init__(self, yardage_value_calculator: StatisticalValueCalculator,
                 minimum_inclusive_required_yardage: int) -> None:
        super().__init__()
        self.yardage_value_calculator = yardage_value_calculator
        self.minimum_inclusive_required_yardage = minimum_inclusive_required_yardage

    def calculate_value(self, statistics: OffensiveStatistics):
        return self.minimum_inclusive_required_yardage <= \
               self.yardage_value_calculator.calculate_value(statistics=statistics)

    def __eq__(self, o: object) -> bool:
        if isinstance(o, HasAchievedMinimumYardageRequirementCalculator):
            return self.yardage_value_calculator == o.yardage_value_calculator and \
                   o.minimum_inclusive_required_yardage == self.minimum_inclusive_required_yardage and super().__eq__(o)

        return False

    def __hash__(self) -> int:
        return hash(
            (self.yardage_value_calculator,
             self.minimum_inclusive_required_yardage,
             super().__hash__()))


class InterceptionsCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.turnovers.interceptions


class RushingTouchdownsCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.scoring.touchdowns.rushing


class RushingYardageCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.yards.rushing


class ReceivingTouchdownsCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.scoring.touchdowns.receiving


class ReceptionsCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.receptions


class ReceivingYardageCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.yards.receiving


class KickoffsReturnTouchdownsCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.scoring.touchdowns.kick_returns.kickoffs


class PuntReturnTouchdownsCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.scoring.touchdowns.kick_returns.punts


class FieldGoalReturnTouchdownsCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.scoring.touchdowns.kick_returns.field_goals


class FumblesLostCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.turnovers.fumbles_lost


class TwoPointConversionsCaughtCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.scoring.conversions.two_point.caught


class TwoPointConversionsRushedCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.scoring.conversions.two_point.rushed


class TwoPointConversionsThrownCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.scoring.conversions.two_point.thrown


class FumbleRecoveryTouchdownsCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.scoring.touchdowns.fumble_recoveries

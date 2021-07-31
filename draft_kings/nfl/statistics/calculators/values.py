from draft_kings.nfl.statistics.models.offensive import OffensiveStatistics
from shared.calculators.scoring import StatisticalValueCalculator


class PassingTouchdownsValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: OffensiveStatistics):
        return statistics.scoring.touchdown.passing


passing_touchdowns_value_calculator = PassingTouchdownsValueCalculator()
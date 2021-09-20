from daily_fantasy_sports_scoring_calculators.draft_kings.nba.statistics.models import Statistics
from daily_fantasy_sports_scoring_calculators.core.calculators.scoring import ConditionEvaluator
from daily_fantasy_sports_scoring_calculators.core.calculators.scoring import StatisticalValueCalculator


class PointsScoredValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: Statistics):
        return statistics.points_scored


class ThreePointersMadeValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: Statistics):
        return statistics.three_pointers_made


class AssistsValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: Statistics):
        return statistics.assists


class StealsValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: Statistics):
        return statistics.steals


class ReboundsValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: Statistics):
        return statistics.rebounds


class BlocksValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: Statistics):
        return statistics.blocks


class TurnoversValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: Statistics):
        return statistics.turnovers


class DoubleFigureValueCalculator(ConditionEvaluator):
    def __init__( # pylint: disable=too-many-arguments
            self,
            points_scored_value_calculator: StatisticalValueCalculator,
            assists_value_calculator: StatisticalValueCalculator,
            rebounds_value_calculator: StatisticalValueCalculator,
            steals_value_calculator: StatisticalValueCalculator,
            blocks_value_calculator: StatisticalValueCalculator,
            minimum_values_that_must_be_at_least_ten: int):
        if 0 > minimum_values_that_must_be_at_least_ten:
            raise ValueError(
                "minimum values that must be at least ten must be non-negative")

        self.minimum_values_that_must_be_at_least_ten = minimum_values_that_must_be_at_least_ten
        self.calculators = {
            points_scored_value_calculator,
            assists_value_calculator,
            rebounds_value_calculator,
            steals_value_calculator,
            blocks_value_calculator}

    def test(self, value):
        return self.minimum_values_that_must_be_at_least_ten <= sum(map(
            lambda calculator: 10 <= calculator.calculate_value(value), self.calculators))

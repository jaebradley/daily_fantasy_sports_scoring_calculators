from draft_kings.nba.scoring.calculators.value_to_points.calculators import points_scored_points_calculator, \
    three_pointers_made_points_calculator, assists_points_calculator, blocks_points_calculator, \
    steals_points_calculator, \
    rebounds_points_calculator, turnovers_points_calculator, double_double_points_calculator, \
    triple_double_points_calculator
from draft_kings.nba.statistics.calculators import points_scored_value_calculator, \
    three_pointers_made_value_calculator, \
    assists_value_calculator, blocks_value_calculator, steals_value_calculator, rebounds_value_calculator, \
    turnovers_value_calculator, double_double_value_calculator, triple_double_value_calculator
from shared.calculators.scoring import StatisticalCategoryPointsCalculator, ConditionalPointsCalculator, \
    zero_points_calculator


class PointsScoredCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(points_scored_value_calculator, points_scored_points_calculator)


class ThreePointersMadeCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(
            three_pointers_made_value_calculator,
            three_pointers_made_points_calculator)


class StealsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(steals_value_calculator, steals_points_calculator)


class ReboundsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(rebounds_value_calculator, rebounds_points_calculator)


class AssistsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(assists_value_calculator, assists_points_calculator)


class TurnoversCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(turnovers_value_calculator, turnovers_points_calculator)


class BlocksCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(blocks_value_calculator, blocks_points_calculator)


class DoubleDoubleCalculator(ConditionalPointsCalculator):
    def __init__(self):
        super().__init__(
            double_double_points_calculator,
            zero_points_calculator,
            double_double_value_calculator)


class TripleDoubleCalculator(ConditionalPointsCalculator):
    def __init__(self):
        super().__init__(
            triple_double_points_calculator,
            zero_points_calculator,
            triple_double_value_calculator)

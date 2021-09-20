from daily_fantasy_sports_scoring_calculators.core.calculators.scoring import StatisticalCategoryPointsCalculator, \
    ConditionalPointsCalculator, zero_points_calculator
from daily_fantasy_sports_scoring_calculators.draft_kings.nba.scoring.calculators.value_to_points.calculators import \
    points_scored_points_calculator, \
    three_pointers_made_points_calculator, assists_points_calculator, blocks_points_calculator, \
    steals_points_calculator, \
    rebounds_points_calculator, turnovers_points_calculator, double_double_points_calculator, \
    triple_double_points_calculator
from daily_fantasy_sports_scoring_calculators.draft_kings.nba.statistics.calculators \
    import DoubleFigureValueCalculator, \
    PointsScoredValueCalculator, \
    AssistsValueCalculator, \
    ReboundsValueCalculator, \
    StealsValueCalculator, BlocksValueCalculator, TurnoversValueCalculator, ThreePointersMadeValueCalculator


class PointsScoredCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(PointsScoredValueCalculator(), points_scored_points_calculator)


class ThreePointersMadeCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(
            ThreePointersMadeValueCalculator(),
            three_pointers_made_points_calculator)


class StealsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(StealsValueCalculator(), steals_points_calculator)


class ReboundsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(ReboundsValueCalculator(), rebounds_points_calculator)


class AssistsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(AssistsValueCalculator(), assists_points_calculator)


class TurnoversCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(TurnoversValueCalculator(), turnovers_points_calculator)


class BlocksCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(BlocksValueCalculator(), blocks_points_calculator)


class DoubleDoubleCalculator(ConditionalPointsCalculator):
    def __init__(self):
        super().__init__(
            double_double_points_calculator,
            zero_points_calculator,
            DoubleFigureValueCalculator(
                PointsScoredValueCalculator(),
                AssistsValueCalculator(),
                ReboundsValueCalculator(),
                StealsValueCalculator(),
                BlocksValueCalculator(),
                2)
        )


class TripleDoubleCalculator(ConditionalPointsCalculator):
    def __init__(self):
        super().__init__(
            triple_double_points_calculator,
            zero_points_calculator,
            DoubleFigureValueCalculator(
                PointsScoredValueCalculator(),
                AssistsValueCalculator(),
                ReboundsValueCalculator(),
                StealsValueCalculator(),
                BlocksValueCalculator(),
                3)
        )

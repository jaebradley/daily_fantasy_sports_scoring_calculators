from draft_kings.nba.calculators.points import zero_points_calculator
from draft_kings.nfl.statistics.calculators.conditions import HasAchievedLimitEvaluator, \
    has_reached_100_yards_condition_evaluator
from shared.calculators.scoring import PointsCalculator, ConditionalPointsCalculator


class PassingTouchdownsCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return 4 * value


class PassingYardageCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return 0.04 * value


class YardageLimitCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return 3


class HasReached300PassingYardsCalculator(ConditionalPointsCalculator):
    def __init__(self):
        super().__init__(YardageLimitCalculator(), zero_points_calculator,
                         HasAchievedLimitEvaluator(inclusive_limit=300))


class TurnoversCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return -1 * value


class NonPassingTouchdownsCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return 6 * value


class NonPassingYardsCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return 0.1 * value


class HasReached100YardsCalculator(ConditionalPointsCalculator):
    def __init__(self):
        super().__init__(YardageLimitCalculator(), zero_points_calculator,
                         has_reached_100_yards_condition_evaluator)


class ReceptionsCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return value


class TwoPointConversionsCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return 2 * value


passing_touchdowns_points_calculator = PassingTouchdownsCalculator()
non_passing_touchdowns_points_calculator = NonPassingTouchdownsCalculator()
has_reached_100_yards_calculator = HasReached100YardsCalculator()
non_passing_yards_calculator = NonPassingYardsCalculator()
turnovers_calculator = TurnoversCalculator()
two_point_conversions_calculator = TwoPointConversionsCalculator()

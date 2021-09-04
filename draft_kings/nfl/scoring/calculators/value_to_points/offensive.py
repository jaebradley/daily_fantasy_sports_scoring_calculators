from draft_kings.nfl.statistics.calculators.conditions import HasAchievedMinimumValueRequirement
from shared.calculators.scoring import PointsCalculator, ConditionalPointsCalculator
from shared.calculators.scoring import zero_points_calculator


class PassingTouchdownsCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return 4 * value


class PassingYardageCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return 0.04 * value


class YardageLimitAchievedCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return 3


class HasAchievedMinimumYardageRequirementCalculator(
        ConditionalPointsCalculator):
    def __init__(self, minimum_inclusive_required_yardage: int):
        super().__init__(
            YardageLimitAchievedCalculator(),
            zero_points_calculator,
            HasAchievedMinimumValueRequirement(
                minimum_inclusive_required_value=minimum_inclusive_required_yardage))


class HasAchievedAtLeast300YardsCalculator(
        HasAchievedMinimumYardageRequirementCalculator):
    def __init__(self):
        super().__init__(300)


class TurnoversCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return -1 * value


class NonPassingTouchdownsCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return 6 * value


class NonPassingYardsCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return 0.1 * value


class HasAchievedAtLeast100YardsCalculator(
        HasAchievedMinimumYardageRequirementCalculator):
    def __init__(self):
        super().__init__(100)


class ReceptionsCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return value


class TwoPointConversionsCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return 2 * value

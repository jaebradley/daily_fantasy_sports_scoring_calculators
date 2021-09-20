from daily_fantasy_sports_scoring_calculators.draft_kings.nfl.statistics.models.defensive import PointsAllowed
from daily_fantasy_sports_scoring_calculators.core.calculators.scoring import PointsCalculator

points_by_points_allowed = {
    PointsAllowed._0: 10,
    PointsAllowed._1_TO_6: 7,
    PointsAllowed._7_TO_13: 4,
    PointsAllowed._14_TO_20: 1,
    PointsAllowed._21_TO_27: 0,
    PointsAllowed._28_TO_24: -1,
    PointsAllowed._35_OR_MORE: -4
}


class SacksCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return 1 * value


class TurnoversCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return 2 * value


class TouchdownsCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return 6 * value


class SafetiesCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return 2 * value


class BlockedKicksCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return 2 * value


class ConversionReturnsCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        return 2 * value


class PointsAllowedCalculator(PointsCalculator):
    def calculate_points(self, value) -> float:
        points = points_by_points_allowed.get(value)
        if points is None:
            raise ValueError(f"Unknown value: {value}")

        return points

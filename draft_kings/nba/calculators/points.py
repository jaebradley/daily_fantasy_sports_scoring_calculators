from shared.calculators.scoring import PointsCalculator


class ZeroPointsCalculator(PointsCalculator):
    def calculate_points(self, value):
        return 0


class PointsScoredPointsCalculator(PointsCalculator):
    def calculate_points(self, value):
        return value


class ThreePointersMadePointsCalculator(PointsCalculator):
    def calculate_points(self, value):
        return value * 0.5


class AssistsPointsCalculator(PointsCalculator):
    def calculate_points(self, value):
        return value * 1.5


class StealsPointsCalculator(PointsCalculator):
    def calculate_points(self, value):
        return value * 2


class BlocksPointsCalculator(PointsCalculator):
    def calculate_points(self, value):
        return value * 2


class ReboundsPointsCalculator(PointsCalculator):
    def calculate_points(self, value):
        return value * 1.25


class TurnoverPointsCalculator(PointsCalculator):
    def calculate_points(self, value):
        return value * -0.5


class BooleanPointsCalculator(PointsCalculator):
    def __init__(self, points_when_true: float, points_when_false: float):
        self.points_when_true = points_when_true
        self.points_when_false = points_when_false

    def calculate_points(self, value):
        if value is True:
            return self.points_when_true

        if value is False:
            return self.points_when_false

        raise ValueError("unknown value: {value}".format(value=value))


points_scored_points_calculator = PointsScoredPointsCalculator()
three_pointers_made_points_calculator = ThreePointersMadePointsCalculator()
assists_points_calculator = AssistsPointsCalculator()
steals_points_calculator = StealsPointsCalculator()
blocks_points_calculator = BlocksPointsCalculator()
turnovers_points_calculator = TurnoverPointsCalculator()
rebounds_points_calculator = ReboundsPointsCalculator()
double_double_points_calculator = BooleanPointsCalculator(1.5, 0)
triple_double_points_calculator = BooleanPointsCalculator(3, 0)
zero_points_calculator = ZeroPointsCalculator()

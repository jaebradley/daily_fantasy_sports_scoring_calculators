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


class DoubleDoublePointsCalculator(PointsCalculator):
    def calculate_points(self, value):
        return 1.5


class TripleDoublePointsCalculator(PointsCalculator):
    def calculate_points(self, value):
        return 3


points_scored_points_calculator = PointsScoredPointsCalculator()
three_pointers_made_points_calculator = ThreePointersMadePointsCalculator()
assists_points_calculator = AssistsPointsCalculator()
steals_points_calculator = StealsPointsCalculator()
blocks_points_calculator = BlocksPointsCalculator()
turnovers_points_calculator = TurnoverPointsCalculator()
rebounds_points_calculator = ReboundsPointsCalculator()
double_double_points_calculator = DoubleDoublePointsCalculator()
triple_double_points_calculator = TripleDoublePointsCalculator()
zero_points_calculator = ZeroPointsCalculator()

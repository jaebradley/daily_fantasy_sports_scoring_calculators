from shared.calculators.scoring import PointsCalculator


class PassingTouchdownsCalculator(PointsCalculator):
    def calculate_points(self, value):
        return value * 4


passing_touchdowns_calculator = PassingTouchdownsCalculator()

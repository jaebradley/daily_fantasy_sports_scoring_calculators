from draft_kings.nba.calculators.scoring.classic import points_calculator as classic_points_calculator
from shared.calculators.scoring import CaptainGameTypePointsCalculator


class PointsCalculator(CaptainGameTypePointsCalculator):
    def __init__(self):
        super().__init__(
            classic_points_calculator,
            1.5,
            1.0
        )


points_calculator = PointsCalculator()

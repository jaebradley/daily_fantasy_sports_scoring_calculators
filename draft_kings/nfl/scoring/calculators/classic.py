from draft_kings.nfl.scoring.rules.offensive import PassingTouchdownsRule
from shared.calculators.scoring import GameTypePointsCalculator


class PointsCalculator(GameTypePointsCalculator):
    def __init__(self):
        super().__init__({
            PassingTouchdownsRule()
        })


points_calculator = PointsCalculator()

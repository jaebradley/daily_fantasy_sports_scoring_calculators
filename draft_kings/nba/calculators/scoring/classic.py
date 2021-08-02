from draft_kings.nba.rules import PointsScoredConditionalPointsCalculator, ThreePointersMadeConditionalPointsCalculator, AssistsConditionalPointsCalculator, BlocksConditionalPointsCalculator, StealsConditionalPointsCalculator, \
    ReboundsConditionalPointsCalculator, TurnoversConditionalPointsCalculator, DoubleDoubleConditionalPointsCalculator, TripleDoubleConditionalPointsCalculator
from shared.calculators.scoring import GameTypePointsCalculator


class PointsCalculator(GameTypePointsCalculator):
    def __init__(self):
        super().__init__(
            {
                PointsScoredConditionalPointsCalculator(),
                ThreePointersMadeConditionalPointsCalculator(),
                AssistsConditionalPointsCalculator(),
                BlocksConditionalPointsCalculator(),
                StealsConditionalPointsCalculator(),
                ReboundsConditionalPointsCalculator(),
                TurnoversConditionalPointsCalculator(),
                DoubleDoubleConditionalPointsCalculator(),
                TripleDoubleConditionalPointsCalculator()
            }
        )


points_calculator = PointsCalculator()

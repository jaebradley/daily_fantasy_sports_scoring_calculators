from draft_kings.nba.scoring.calculators.statistical_value_to_points.calculators import PointsScoredCalculator, \
    ThreePointersMadeCalculator, AssistsCalculator, BlocksCalculator, StealsCalculator, \
    ReboundsCalculator, TurnoversCalculator, DoubleDoubleCalculator, TripleDoubleCalculator
from shared.calculators.scoring import GameTypePointsCalculator


class PointsCalculator(GameTypePointsCalculator):
    def __init__(self):
        super().__init__(
            {
                PointsScoredCalculator(),
                ThreePointersMadeCalculator(),
                AssistsCalculator(),
                BlocksCalculator(),
                StealsCalculator(),
                ReboundsCalculator(),
                TurnoversCalculator(),
                DoubleDoubleCalculator(),
                TripleDoubleCalculator()
            }
        )


points_calculator = PointsCalculator()

from draft_kings.nba.classic.calculators.scoring.calculators import PointsScoredRule, ThreePointersMadeRule, \
    AssistsRule, \
    BlocksRule, StealsRule, ReboundsRule, TurnoversRule, DoubleDoubleRule, TripleDoubleRule
from shared.calculators.scoring import GameTypePointsCalculator


class PointsCalculator(GameTypePointsCalculator):
    def __init__(self):
        super().__init__(
            {
                PointsScoredRule(),
                ThreePointersMadeRule(),
                AssistsRule(),
                BlocksRule(),
                StealsRule(),
                ReboundsRule(),
                TurnoversRule(),
                DoubleDoubleRule(),
                TripleDoubleRule()
            }
        )


points_calculator = PointsCalculator()

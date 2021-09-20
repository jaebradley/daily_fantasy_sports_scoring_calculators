from daily_fantasy_sports_scoring_calculators.draft_kings.nba.scoring.calculators.game_types.classic import \
    points_calculator as classic_points_calculator
from daily_fantasy_sports_scoring_calculators.core.calculators.scoring import CaptainGameTypePointsCalculator


class PointsCalculator(CaptainGameTypePointsCalculator):
    def __init__(self):
        super().__init__(
            classic_points_calculator,
            1.5,
            1.0
        )


points_calculator = PointsCalculator()

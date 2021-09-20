from daily_fantasy_sports_scoring_calculators.draft_kings.nfl.scoring.calculators.statistical_value_to_points.defensive import SacksCalculator, \
    InterceptionsCalculator, FumbleRecoveriesCalculator, PuntReturnTouchdownsCalculator, \
    KickoffReturnTouchdownsCalculator, FieldGoalReturnTouchdownsCalculator, InterceptionReturnTouchdownsCalculator, \
    FumbleRecoveryTouchdownsCalculator, BlockedPuntReturnTouchdownsCalculator, \
    BlockedFieldGoalReturnTouchdownsCalculator, \
    SafetiesCalculator, BlockedKicksCalculator, ConversionReturnsCalculator, PointsAllowedCalculator
from shared.calculators.scoring import GameTypePointsCalculator


class PointsCalculator(GameTypePointsCalculator):
    def __init__(self):
        super().__init__({
            SacksCalculator(),
            FumbleRecoveriesCalculator(),
            InterceptionsCalculator(),
            PuntReturnTouchdownsCalculator(),
            KickoffReturnTouchdownsCalculator(),
            FieldGoalReturnTouchdownsCalculator(),
            InterceptionReturnTouchdownsCalculator(),
            FumbleRecoveryTouchdownsCalculator(),
            BlockedPuntReturnTouchdownsCalculator(),
            BlockedFieldGoalReturnTouchdownsCalculator(),
            SafetiesCalculator(),
            BlockedKicksCalculator(),
            ConversionReturnsCalculator(),
            PointsAllowedCalculator()
        })


points_calculator = PointsCalculator()

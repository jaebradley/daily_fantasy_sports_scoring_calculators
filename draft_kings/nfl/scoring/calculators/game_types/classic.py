from draft_kings.nfl.scoring.calculators.statistical_value_to_points.offensive import PassingTouchdownsPointsCalculator, \
    HasReached300YardPassingYardageLimitPointsCalculator, PassingYardagePointsCalculator, \
    HasReached100YardsRushingPointsLimit, InterceptionsCalculator, RushingTouchdownsCalculator, \
    RushingYardageCalculator, ReceivingTouchdownsCalculator, ReceivingYardsCalculator, \
    HasReached100YardsReceivingCalculator, ReceptionsCalculator, PuntReturnTouchdownsCalculator, \
    KickReturnTouchdownsCalculator, FieldGoalReturnTouchdownsCalculator, FumblesLostCalculator, \
    TwoPointConversionsPassedCalculator, TwoPointConversionsCaughtCalculator, TwoPointConversionsRushedCalculator, \
    FumbleRecoveryTouchdownsCalculator
from shared.calculators.scoring import GameTypePointsCalculator


class PointsCalculator(GameTypePointsCalculator):
    def __init__(self):
        super().__init__({
            PassingTouchdownsPointsCalculator(),
            PassingYardagePointsCalculator(),
            HasReached300YardPassingYardageLimitPointsCalculator(),
            InterceptionsCalculator(),
            HasReached100YardsRushingPointsLimit(),
            RushingTouchdownsCalculator(),
            RushingYardageCalculator(),
            ReceivingTouchdownsCalculator(),
            ReceivingYardsCalculator(),
            HasReached100YardsReceivingCalculator(),
            ReceptionsCalculator(),
            PuntReturnTouchdownsCalculator(),
            KickReturnTouchdownsCalculator(),
            FieldGoalReturnTouchdownsCalculator(),
            FumblesLostCalculator(),
            TwoPointConversionsPassedCalculator(),
            TwoPointConversionsCaughtCalculator(),
            TwoPointConversionsRushedCalculator(),
            FumbleRecoveryTouchdownsCalculator()
        })


points_calculator = PointsCalculator()

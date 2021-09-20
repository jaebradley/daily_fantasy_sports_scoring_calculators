from daily_fantasy_sports_scoring_calculators.draft_kings.nfl.scoring.calculators \
    .statistical_value_to_points.offensive import PassingTouchdownsCalculator, \
    HasAchievedAtLeast300PassingYardsCalculator, PassingYardageCalculator, \
    HasReached100YardsRushingPointsLimit, InterceptionsCalculator, RushingTouchdownsCalculator, \
    RushingYardageCalculator, ReceivingTouchdownsCalculator, ReceivingYardsCalculator, \
    HasReached100YardsReceivingCalculator, ReceptionsCalculator, PuntReturnTouchdownsCalculator, \
    KickReturnTouchdownsCalculator, FieldGoalReturnTouchdownsCalculator, FumblesLostCalculator, \
    TwoPointConversionsThrownCalculator, TwoPointConversionsCaughtCalculator, TwoPointConversionsRushedCalculator, \
    FumbleRecoveryTouchdownsCalculator
from shared.calculators.scoring import GameTypePointsCalculator


class PointsCalculator(GameTypePointsCalculator):
    def __init__(self):
        super().__init__({
            PassingTouchdownsCalculator(),
            PassingYardageCalculator(),
            HasAchievedAtLeast300PassingYardsCalculator(),
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
            TwoPointConversionsThrownCalculator(),
            TwoPointConversionsCaughtCalculator(),
            TwoPointConversionsRushedCalculator(),
            FumbleRecoveryTouchdownsCalculator()
        })


points_calculator = PointsCalculator()

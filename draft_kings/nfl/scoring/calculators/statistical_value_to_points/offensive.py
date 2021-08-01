from draft_kings.nfl.scoring.calculators.value_to_points.offensive import passing_touchdowns_points_calculator, \
    HasReached300PassingYardsCalculator, PassingYardageCalculator, HasReached100YardsCalculator, \
    non_passing_touchdowns_points_calculator, \
    NonPassingYardsCalculator as RushingYardsPointsCalculator, non_passing_yards_calculator as \
    non_passing_yards_points_calculator, turnovers_calculator as turnovers_points_calculator, \
    two_point_conversions_calculator as two_point_conversions_points_calculator, ReceptionsCalculator as \
    ReceptionsPointsCalculator
from draft_kings.nfl.statistics.calculators.values import passing_touchdowns_value_calculator, \
    at_least_300_yards_passing_value_calculator, passing_yardage_value_calculator, \
    at_least_100_yards_rushing_calculator, InterceptionsValueCalculator, RushingTouchdownsValueCalculator, \
    RushingYardageValueCalculator, ReceivingTouchdownsValueCalculator, ReceptionsValueCalculator, \
    KickoffsReturnTouchdownsValueCalculator, PuntReturnTouchdownsValueCalculator, \
    FieldGoalReturnTouchdownsValueCalculator, FumblesLostValueCalculator, TwoPointConversionsCaughtValueCalculator, \
    TwoPointConversionsRushedValueCalculator, TwoPointConversionsThrownValueCalculator, \
    FumbleRecoveryTouchdownsValueCalculator, ReceivingYardageValueCalculator, at_least_100_yards_receiving_calculator
from shared.calculators.scoring import StatisticalCategoryPointsCalculator, StatisticalValueCalculator


class PassingTouchdownsPointsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(passing_touchdowns_value_calculator, passing_touchdowns_points_calculator)


class NonPassingTouchdownsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self, value_calculator: StatisticalValueCalculator):
        super().__init__(value_calculator, non_passing_touchdowns_points_calculator)


class HasReached300YardPassingYardageLimitPointsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(
            at_least_300_yards_passing_value_calculator,
            HasReached300PassingYardsCalculator()
        )


class PassingYardagePointsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(passing_yardage_value_calculator, PassingYardageCalculator())


class TurnoversCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self, value_calculator: StatisticalValueCalculator):
        super().__init__(value_calculator, turnovers_points_calculator)


class InterceptionsCalculator(TurnoversCalculator):
    def __init__(self):
        super().__init__(InterceptionsValueCalculator())


class RushingTouchdownsCalculator(NonPassingTouchdownsCalculator):
    def __init__(self):
        super().__init__(RushingTouchdownsValueCalculator())


class RushingYardageCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(RushingYardageValueCalculator(), RushingYardsPointsCalculator())


class HasReached100YardsRushingPointsLimit(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(at_least_100_yards_rushing_calculator, HasReached100YardsCalculator())


class ReceivingTouchdownsCalculator(NonPassingTouchdownsCalculator):
    def __init__(self):
        super().__init__(ReceivingTouchdownsValueCalculator())


class ReceivingYardsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(ReceivingYardageValueCalculator(), non_passing_yards_points_calculator)


class HasReached100YardsReceivingCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(value_calculator=at_least_100_yards_receiving_calculator,
                         points_calculator=HasReached100YardsCalculator())


class ReceptionsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(ReceptionsValueCalculator(), ReceptionsPointsCalculator())


class PuntReturnTouchdownsCalculator(NonPassingTouchdownsCalculator):
    def __init__(self):
        super().__init__(PuntReturnTouchdownsValueCalculator())


class KickReturnTouchdownsCalculator(NonPassingTouchdownsCalculator):
    def __init__(self):
        super().__init__(KickoffsReturnTouchdownsValueCalculator())


class FieldGoalReturnTouchdownsCalculator(NonPassingTouchdownsCalculator):
    def __init__(self):
        super().__init__(FieldGoalReturnTouchdownsValueCalculator())


class FumblesLostCalculator(TurnoversCalculator):
    def __init__(self):
        super().__init__(FumblesLostValueCalculator())


class TwoPointConversionCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self, value_calculator: StatisticalValueCalculator):
        super().__init__(value_calculator, two_point_conversions_points_calculator)


class TwoPointConversionsPassedCalculator(TwoPointConversionCalculator):
    def __init__(self):
        super().__init__(TwoPointConversionsThrownValueCalculator())


class TwoPointConversionsCaughtCalculator(TwoPointConversionCalculator):
    def __init__(self):
        super().__init__(TwoPointConversionsCaughtValueCalculator())


class TwoPointConversionsRushedCalculator(TwoPointConversionCalculator):
    def __init__(self):
        super().__init__(TwoPointConversionsRushedValueCalculator())


class FumbleRecoveryTouchdownsCalculator(NonPassingTouchdownsCalculator):
    def __init__(self):
        super().__init__(FumbleRecoveryTouchdownsValueCalculator())

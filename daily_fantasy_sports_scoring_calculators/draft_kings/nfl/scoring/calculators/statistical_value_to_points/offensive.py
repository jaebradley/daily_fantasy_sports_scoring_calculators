from daily_fantasy_sports_scoring_calculators.draft_kings.nfl.scoring.calculators.value_to_points.offensive import \
    PassingTouchdownsCalculator as PassingTouchdownsPointsCalculator, \
    HasAchievedAtLeast300YardsCalculator as HasAchievedAtLeast300PassingYardsPointsCalculator, \
    PassingYardageCalculator as PassingYardagePointsCalculator, \
    HasAchievedAtLeast100YardsCalculator as HasAchievedAtLeast100YardsPointsCalculator, \
    NonPassingTouchdownsCalculator as NonPassingTouchdownsPointsCalculator, \
    NonPassingYardsCalculator as NonPassingYardsPointsCalculator, \
    TurnoversCalculator as TurnoversPointsCalculator, \
    TwoPointConversionsCalculator as TwoPointConversionsPointsCalculator, \
    ReceptionsCalculator as ReceptionsPointsCalculator
from daily_fantasy_sports_scoring_calculators.draft_kings.nfl.statistics.calculators.offensive import \
    PassingTouchdownsCalculator as PassingTouchdownsValueCalculator, \
    HasAchievedMinimumYardageRequirementCalculator as HasAchievedMinimumYardageRequirementValueCalculator, \
    InterceptionsCalculator as InterceptionsValueCalculator, \
    RushingTouchdownsCalculator as RushingTouchdownsValueCalculator, \
    RushingYardageCalculator as RushingYardageValueCalculator, \
    ReceivingTouchdownsCalculator as ReceivingTouchdownsValueCalculator, \
    ReceptionsCalculator as ReceptionsValueCalculator, \
    KickoffsReturnTouchdownsCalculator as KickoffsReturnTouchdownsValueCalculator, \
    PuntReturnTouchdownsCalculator as PuntReturnTouchdownsValueCalculator, \
    FieldGoalReturnTouchdownsCalculator as FieldGoalReturnTouchdownsValueCalculator, \
    FumblesLostCalculator as FumblesLostValueCalculator, \
    TwoPointConversionsCaughtCalculator as TwoPointConversionsCaughtValueCalculator, \
    TwoPointConversionsRushedCalculator as TwoPointConversionsRushedValueCalculator, \
    TwoPointConversionsThrownCalculator as TwoPointConversionsThrownValueCalculator, \
    FumbleRecoveryTouchdownsCalculator as FumbleRecoveryTouchdownsValueCalculator, \
    ReceivingYardageCalculator as ReceivingYardageValueCalculator, \
    PassingYardageCalculator as PassingYardageValueCalculator
from shared.calculators.scoring import StatisticalCategoryPointsCalculator, StatisticalValueCalculator

passing_yardage_value_calculator = PassingYardageValueCalculator()
receiving_yardage_value_calculator = ReceivingYardageValueCalculator()
rushing_yardage_value_calculator = RushingYardageValueCalculator()

non_passing_yards_points_calculator = NonPassingYardsPointsCalculator()


class PassingTouchdownsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(
            PassingTouchdownsValueCalculator(),
            PassingTouchdownsPointsCalculator())


class NonPassingTouchdownsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self, value_calculator: StatisticalValueCalculator):
        super().__init__(value_calculator, NonPassingTouchdownsPointsCalculator())


class HasAchievedAtLeast300PassingYardsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(
            HasAchievedMinimumYardageRequirementValueCalculator(
                yardage_value_calculator=passing_yardage_value_calculator,
                minimum_inclusive_required_yardage=300
            ),
            HasAchievedAtLeast300PassingYardsPointsCalculator()
        )


class PassingYardageCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(
            passing_yardage_value_calculator,
            PassingYardagePointsCalculator())


class TurnoversCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self, value_calculator: StatisticalValueCalculator):
        super().__init__(value_calculator, TurnoversPointsCalculator())

    def __eq__(self, o: object) -> bool:
        if isinstance(o, TurnoversCalculator):
            return o.value_calculator == self.value_calculator and super().__eq__(o)

        return False

    def __hash__(self):
        return hash((self.value_calculator, super().__hash__()))


class InterceptionsCalculator(TurnoversCalculator):
    def __init__(self):
        super().__init__(InterceptionsValueCalculator())


class RushingTouchdownsCalculator(NonPassingTouchdownsCalculator):
    def __init__(self):
        super().__init__(RushingTouchdownsValueCalculator())


class RushingYardageCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(
            rushing_yardage_value_calculator,
            non_passing_yards_points_calculator)


class HasReached100YardsRushingPointsLimit(
    StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(
            HasAchievedMinimumYardageRequirementValueCalculator(
                yardage_value_calculator=rushing_yardage_value_calculator,
                minimum_inclusive_required_yardage=100
            ),
            HasAchievedAtLeast100YardsPointsCalculator()
        )


class ReceivingTouchdownsCalculator(NonPassingTouchdownsCalculator):
    def __init__(self):
        super().__init__(ReceivingTouchdownsValueCalculator())


class ReceivingYardsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(
            receiving_yardage_value_calculator,
            non_passing_yards_points_calculator)


class HasReached100YardsReceivingCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(
            value_calculator=HasAchievedMinimumYardageRequirementValueCalculator(
                yardage_value_calculator=receiving_yardage_value_calculator,
                minimum_inclusive_required_yardage=100),
            points_calculator=HasAchievedAtLeast100YardsPointsCalculator())


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
        super().__init__(value_calculator, TwoPointConversionsPointsCalculator())

    def __eq__(self, o: object) -> bool:
        if isinstance(o, TwoPointConversionCalculator):
            return o.value_calculator == self.value_calculator and super().__eq__(o)

        return False

    def __hash__(self):
        return hash((self.value_calculator, super().__hash__()))


class TwoPointConversionsThrownCalculator(TwoPointConversionCalculator):
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

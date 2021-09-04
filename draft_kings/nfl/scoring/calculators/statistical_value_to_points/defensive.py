from draft_kings.nfl.scoring.calculators.value_to_points.defensive import SacksCalculator as SacksPointsCalculator, \
    TurnoversCalculator as TurnoversPointsCalculator, TouchdownsCalculator as TouchdownsPointsCalculator, \
    SafetiesCalculator as SafetiesPointsCalculator, BlockedKicksCalculator as BlockedKicksPointsCalculator, \
    ConversionReturnsCalculator as ConversionReturnsPointsCalculator, PointsAllowedCalculator as \
    PointsAllowedPointsCalculator
from draft_kings.nfl.statistics.calculators.defensive import SacksCalculator as SacksValueCalculator, \
    InterceptionsCalculator as InterceptionsValueCalculator, \
    FumbleRecoveriesCalculator as FumbleRecoversValueCalculator, \
    PuntReturnTouchdownsCalculator as PuntReturnTouchdownsValueCalculator, \
    KickoffReturnTouchdownsCalculator as KickoffReturnTouchdownsValueCalculator, \
    FieldGoalReturnTouchdownsCalculator as FieldGoalReturnTouchdownsValueCalculator, \
    InterceptionReturnTouchdownsCalculator as InterceptionReturnTouchdownsValueCalculator, \
    FumbleRecoveryTouchdownsCalculator as FumbleRecoveryTouchdownsValueCalculator, \
    BlockedPuntReturnTouchdownsCalculator as BlockedPuntReturnTouchdownsValueCalculator, \
    BlockedFieldGoalReturnTouchdownsCalculator as BlockedFieldGoalReturnTouchdownsValueCalculator, \
    SafetiesCalculator as SafetiesValueCalculator, \
    BlockedKicksCalculator as BlockedKicksValueCalculator, \
    ConversionReturnsCalculator as ConversionReturnsValueCalculator, \
    PointsAllowedCalculator as PointsAllowedValueCalculator
from shared.calculators.scoring import StatisticalCategoryPointsCalculator

turnovers_points_calculator = TurnoversPointsCalculator()
touchdowns_points_calculator = TouchdownsPointsCalculator()


class SacksCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(SacksValueCalculator(), SacksPointsCalculator())


class InterceptionsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(InterceptionsValueCalculator(), turnovers_points_calculator)


class FumbleRecoveriesCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(FumbleRecoversValueCalculator(), turnovers_points_calculator)


class PuntReturnTouchdownsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(
            PuntReturnTouchdownsValueCalculator(),
            touchdowns_points_calculator)


class KickoffReturnTouchdownsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(
            KickoffReturnTouchdownsValueCalculator(),
            touchdowns_points_calculator)


class FieldGoalReturnTouchdownsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(
            FieldGoalReturnTouchdownsValueCalculator(),
            touchdowns_points_calculator)


class InterceptionReturnTouchdownsCalculator(
        StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(
            InterceptionReturnTouchdownsValueCalculator(),
            touchdowns_points_calculator)


class FumbleRecoveryTouchdownsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(
            FumbleRecoveryTouchdownsValueCalculator(),
            touchdowns_points_calculator)


class BlockedPuntReturnTouchdownsCalculator(
        StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(
            BlockedPuntReturnTouchdownsValueCalculator(),
            touchdowns_points_calculator)


class BlockedFieldGoalReturnTouchdownsCalculator(
        StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(
            BlockedFieldGoalReturnTouchdownsValueCalculator(),
            touchdowns_points_calculator)


class SafetiesCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(SafetiesValueCalculator(), SafetiesPointsCalculator())


class BlockedKicksCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(BlockedKicksValueCalculator(), BlockedKicksPointsCalculator())


class ConversionReturnsCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(
            ConversionReturnsValueCalculator(),
            ConversionReturnsPointsCalculator())


class PointsAllowedCalculator(StatisticalCategoryPointsCalculator):
    def __init__(self):
        super().__init__(PointsAllowedValueCalculator(), PointsAllowedPointsCalculator())

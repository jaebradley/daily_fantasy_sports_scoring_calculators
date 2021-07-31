from draft_kings.nba.calculators.points import zero_points_calculator
from draft_kings.nfl.scoring.calculators.points import passing_touchdowns_calculator
from draft_kings.nfl.statistics.calculators.values import passing_touchdowns_value_calculator
from shared.calculators.scoring import Rule
from shared.validators import always_true_validator


class PassingTouchdownsRule(Rule):
    def __init__(self):
        super().__init__(passing_touchdowns_calculator, zero_points_calculator, always_true_validator,
                         passing_touchdowns_value_calculator)

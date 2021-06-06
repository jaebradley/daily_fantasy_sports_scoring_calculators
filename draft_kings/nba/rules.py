from draft_kings.nba.calculators.points import points_scored_points_calculator, zero_points_calculator, \
    three_pointers_made_points_calculator, assists_points_calculator, blocks_points_calculator, \
    steals_points_calculator, \
    rebounds_points_calculator, turnovers_points_calculator, double_double_points_calculator, \
    triple_double_points_calculator
from draft_kings.nba.calculators.values import points_scored_value_calculator, three_pointers_made_value_calculator, \
    assists_value_calculator, blocks_value_calculator, steals_value_calculator, rebounds_value_calculator, \
    turnovers_value_calculator, double_double_value_calculator, triple_double_value_calculator
from shared.calculators.scoring import Rule
from shared.validators import always_true_validator, identity_validator


class PointsScoredRule(Rule):
    def __init__(self):
        super().__init__(points_scored_points_calculator, zero_points_calculator, always_true_validator,
                         points_scored_value_calculator)


class ThreePointersMadeRule(Rule):
    def __init__(self):
        super().__init__(three_pointers_made_points_calculator, zero_points_calculator, always_true_validator,
                         three_pointers_made_value_calculator)


class AssistsRule(Rule):
    def __init__(self):
        super().__init__(assists_points_calculator, zero_points_calculator, always_true_validator,
                         assists_value_calculator)


class BlocksRule(Rule):
    def __init__(self):
        super().__init__(blocks_points_calculator, zero_points_calculator, always_true_validator,
                         blocks_value_calculator)


class StealsRule(Rule):
    def __init__(self):
        super().__init__(steals_points_calculator, zero_points_calculator, always_true_validator,
                         steals_value_calculator)


class ReboundsRule(Rule):
    def __init__(self):
        super().__init__(rebounds_points_calculator, zero_points_calculator, always_true_validator,
                         rebounds_value_calculator)


class TurnoversRule(Rule):
    def __init__(self):
        super().__init__(turnovers_points_calculator, zero_points_calculator, always_true_validator,
                         turnovers_value_calculator)


class DoubleDoubleRule(Rule):
    def __init__(self):
        super().__init__(double_double_points_calculator, zero_points_calculator, identity_validator,
                         double_double_value_calculator)


class TripleDoubleRule(Rule):
    def __init__(self):
        super().__init__(triple_double_points_calculator, zero_points_calculator, identity_validator,
                         triple_double_value_calculator)
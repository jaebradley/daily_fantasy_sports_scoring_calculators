from draft_kings.nba.classic.calculators.scoring.validators import always_true_validator, identity_validator
from shared.calculators.scoring import PointsCalculator
from shared.calculators.scoring import Rule
from shared.calculators.scoring import StatisticalValueCalculator


class ClassicStatistics:
    def __init__(self, points_scored, three_pointers_made, assists, rebounds, steals, blocks, turnovers):
        self.points_scored = points_scored
        self.three_pointers_made = three_pointers_made
        self.assists = assists
        self.rebounds = rebounds
        self.steals = steals
        self.blocks = blocks
        self.turnovers = turnovers


class PointsScoredPointsCalculator(PointsCalculator):
    def calculate_points(self, value):
        return value


class ThreePointersMadePointsCalculator(PointsCalculator):
    def calculate_points(self, value):
        return value * 0.5


class AssistsPointsCalculator(PointsCalculator):
    def calculate_points(self, value):
        return value * 1.5


class StealsPointsCalculator(PointsCalculator):
    def calculate_points(self, value):
        return value * 2


class BlocksPointsCalculator(PointsCalculator):
    def calculate_points(self, value):
        return value * 2


class ReboundsPointsCalculator(PointsCalculator):
    def calculate_points(self, value):
        return value * 1.25


class TurnoverPointsCalculator(PointsCalculator):
    def calculate_points(self, value):
        return value * -0.5


class BooleanPointsCalculator(PointsCalculator):
    def __init__(self, points_when_true: float, points_when_false: float):
        self.points_when_true = points_when_true
        self.points_when_false = points_when_false

    def calculate_points(self, value):
        if value is True:
            return self.points_when_true

        if value is False:
            return self.points_when_false

        raise ValueError("unknown value: {value}".format(value=value))


class ZeroPointsCalculator(PointsCalculator):
    def calculate_points(self, value):
        return 0


points_scored_points_calculator = PointsScoredPointsCalculator()
three_pointers_made_points_calculator = ThreePointersMadePointsCalculator()
assists_points_calculator = AssistsPointsCalculator()
steals_points_calculator = StealsPointsCalculator()
blocks_points_calculator = BlocksPointsCalculator()
turnovers_points_calculator = TurnoverPointsCalculator()
rebounds_points_calculator = ReboundsPointsCalculator()
double_double_points_calculator = BooleanPointsCalculator(1.5, 0)
triple_double_points_calculator = BooleanPointsCalculator(3, 0)
zero_points_calculator = ZeroPointsCalculator()


class PointsScoredValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: ClassicStatistics):
        return statistics.points_scored


class ThreePointersMadeValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: ClassicStatistics):
        return statistics.three_pointers_made


class AssistsValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: ClassicStatistics):
        return statistics.assists


class StealsValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: ClassicStatistics):
        return statistics.steals


class ReboundsValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: ClassicStatistics):
        return statistics.rebounds


class BlocksValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: ClassicStatistics):
        return statistics.blocks


class TurnoversValueCalculator(StatisticalValueCalculator):
    def calculate_value(self, statistics: ClassicStatistics):
        return statistics.turnovers


class DoubleFigureValueCalculator(StatisticalValueCalculator):
    def __init__(self, points_scored_value_calculator: StatisticalValueCalculator, assists_value_calculator:
    StatisticalValueCalculator, rebounds_value_calculator: StatisticalValueCalculator, steals_value_calculator:
    StatisticalValueCalculator, blocks_value_calculator: StatisticalValueCalculator,
                 minimum_values_that_must_be_at_least_ten: int):
        self.minimum_values_that_must_be_at_least_ten = minimum_values_that_must_be_at_least_ten
        self.calculators = {points_scored_value_calculator, assists_value_calculator, rebounds_value_calculator,
                            steals_value_calculator, blocks_value_calculator}

    def calculate_value(self, statistics):
        return self.minimum_values_that_must_be_at_least_ten <= sum(
            map(lambda calculator: 10 <= calculator.calculate_value(statistics), self.calculators))


points_scored_value_calculator = PointsScoredValueCalculator()
three_pointers_made_value_calculator = ThreePointersMadeValueCalculator()
assists_value_calculator = AssistsValueCalculator()
blocks_value_calculator = BlocksValueCalculator()
steals_value_calculator = StealsValueCalculator()
rebounds_value_calculator = ReboundsValueCalculator()
turnovers_value_calculator = TurnoversValueCalculator()
double_double_value_calculator = DoubleFigureValueCalculator(
    points_scored_value_calculator, assists_value_calculator, rebounds_value_calculator,
    steals_value_calculator, blocks_value_calculator, 2
)
triple_double_value_calculator = DoubleFigureValueCalculator(
    points_scored_value_calculator, assists_value_calculator, rebounds_value_calculator,
    steals_value_calculator, blocks_value_calculator, 3
)


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

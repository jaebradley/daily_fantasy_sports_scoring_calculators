from typing import Set


class StatisticalValueCalculator:
    def calculate_value(self, statistics):
        raise NotImplementedError()


class PointsCalculator:
    def calculate_points(self, value):
        raise NotImplementedError()


class RuleValidator:
    def test(self, statistics):
        raise NotImplementedError()


class Rule:
    def __init__(self, points_calculator_when_rule_is_true: PointsCalculator,
                 points_calculator_when_rule_is_false: PointsCalculator, validator: RuleValidator,
                 value_calculator: StatisticalValueCalculator):
        self.points_calculator_when_rule_is_true = points_calculator_when_rule_is_true
        self.points_calculator_when_rule_is_false = points_calculator_when_rule_is_false
        self.validator = validator
        self.value_calculator = value_calculator

    def apply(self, statistics):
        value = self.value_calculator.calculate_value(statistics)

        if self.validator.test(value):
            return self.points_calculator_when_rule_is_true.calculate_points(value)

        return self.points_calculator_when_rule_is_false.calculate_points(value)

    def __eq__(self, other):
        if isinstance(other, Rule):
            return other.points_calculator_when_rule_is_true == self.points_calculator_when_rule_is_true \
                   and other.points_calculator_when_rule_is_false == self.points_calculator_when_rule_is_false \
                   and other.validator == self.validator and other.value_calculator == self.value_calculator

        return False


class GameTypePointsCalculator(PointsCalculator):
    def __init__(self, rules: Set[Rule]):
        self.rules = rules

    def calculate_points(self, statistics):
        return sum(
            map(
                lambda rule: rule.apply(statistics),
                self.rules
            )
        )

from typing import Set


class StatisticalValueCalculator:
    def calculate_value(self, statistics):
        raise NotImplementedError()


class ConditionalValueEvaluator:
    def test(self, value):
        raise NotImplementedError()


class PointsCalculator:
    def calculate_points(self, value) -> float:
        raise NotImplementedError()


class ConditionalPointsCalculator(PointsCalculator):
    def __init__(self, points_calculator_when_condition_is_true: PointsCalculator,
                 points_calculator_when_condition_is_false: PointsCalculator,
                 condition_evaluator: ConditionalValueEvaluator
                 ):
        self.points_calculator_when_rule_is_true = points_calculator_when_condition_is_true
        self.points_calculator_when_rule_is_false = points_calculator_when_condition_is_false
        self.validator = condition_evaluator

    def calculate_points(self, value) -> float:
        condition = self.validator.test(value=value)
        if True is condition:
            return self.points_calculator_when_rule_is_true.calculate_points(value)

        if False is condition:
            return self.points_calculator_when_rule_is_false.calculate_points(value)

        raise ValueError(f"Unknown condition: {condition}")


class CaptainPointsCalculator:
    def calculate_points(self, value, is_captain: bool):
        raise NotImplementedError()


class StatisticalCategoryPointsCalculator:
    def __init__(self, value_calculator: StatisticalValueCalculator, points_calculator: PointsCalculator):
        self.value_calculator = value_calculator
        self.points_calculator = points_calculator

    def calculate_points(self, statistics):
        return self.points_calculator.calculate_points(value=self.value_calculator.calculate_value(statistics))


class GameTypePointsCalculator(PointsCalculator):
    def __init__(self, calculators: Set[StatisticalCategoryPointsCalculator]):
        self.calculators = calculators

    def calculate_points(self, statistics):
        return sum(
            map(
                lambda calculator: calculator.apply(statistics),
                self.calculators
            )
        )


class CaptainGameTypePointsCalculator(CaptainPointsCalculator):
    def __init__(self, statistical_points_calculator: GameTypePointsCalculator, points_modifier_when_captain: float,
                 points_modifier_when_not_captain: float):
        self.statistical_points_calculator = statistical_points_calculator
        self.points_modifier_when_captain = points_modifier_when_captain
        self.points_modifier_when_not_captain = points_modifier_when_not_captain

    def calculate_points(self, value, is_captain: bool):
        points = self.statistical_points_calculator.calculate_points(value)
        if is_captain is True:
            return self.points_modifier_when_captain * points

        return self.points_modifier_when_not_captain * points

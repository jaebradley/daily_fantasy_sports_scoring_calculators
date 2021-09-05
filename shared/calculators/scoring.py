from typing import Set


class StatisticalValueCalculator:
    def calculate_value(self, statistics):
        raise NotImplementedError()


class ConditionEvaluator:
    def test(self, value) -> bool:
        raise NotImplementedError()


class PointsCalculator:
    def calculate_points(self, value) -> float:
        raise NotImplementedError()


class ConditionalPointsCalculator(PointsCalculator):
    def __init__(
            self,
            points_calculator_when_condition_is_met: PointsCalculator,
            points_calculator_when_condition_is_not_met: PointsCalculator,
            condition_evaluator: ConditionEvaluator):
        self.points_calculator_when_condition_is_met = points_calculator_when_condition_is_met
        self.points_calculator_when_condition_is_not_met = points_calculator_when_condition_is_not_met
        self.condition_evaluator = condition_evaluator

    def calculate_points(self, value) -> float:
        has_condition_been_met = self.condition_evaluator.test(value=value)
        if True is has_condition_been_met:
            return self.points_calculator_when_condition_is_met.calculate_points(
                value)

        if False is has_condition_been_met:
            return self.points_calculator_when_condition_is_not_met.calculate_points(
                value)

        raise ValueError(
            f"Unknown has_condition_been_met: {has_condition_been_met}")


class CaptainPointsCalculator:
    def calculate_points(self, value, is_captain: bool):
        raise NotImplementedError()


class StatisticalCategoryPointsCalculator:
    def __init__(
            self,
            value_calculator: StatisticalValueCalculator,
            points_calculator: PointsCalculator):
        self.value_calculator = value_calculator
        self.points_calculator = points_calculator

    def calculate_points(self, statistics):
        return self.points_calculator.calculate_points(
            value=self.value_calculator.calculate_value(statistics))

    def __eq__(self, o: object) -> bool:
        if isinstance(o, StatisticalCategoryPointsCalculator):
            return self.value_calculator == o.value_calculator and self.points_calculator == o.points_calculator

        return False

    def __hash__(self):
        return hash((self.value_calculator, self.points_calculator))


class GameTypePointsCalculator(PointsCalculator):
    def __init__(self, calculators: Set[StatisticalCategoryPointsCalculator]):
        self.calculators = calculators

    def calculate_points(self, value):
        return sum(
            map(
                lambda calculator: calculator.calculate_points(statistics=value),
                self.calculators
            )
        )


class CaptainGameTypePointsCalculator(CaptainPointsCalculator):
    def __init__(
            self,
            statistical_points_calculator: GameTypePointsCalculator,
            points_modifier_when_captain: float,
            points_modifier_when_not_captain: float):
        self.statistical_points_calculator = statistical_points_calculator
        self.points_modifier_when_captain = points_modifier_when_captain
        self.points_modifier_when_not_captain = points_modifier_when_not_captain

    def calculate_points(self, value, is_captain: bool):
        points = self.statistical_points_calculator.calculate_points(value=value)
        if is_captain is True:
            return self.points_modifier_when_captain * points

        return self.points_modifier_when_not_captain * points


class ZeroPointsCalculator(PointsCalculator):
    def calculate_points(self, value):
        return 0


zero_points_calculator = ZeroPointsCalculator()

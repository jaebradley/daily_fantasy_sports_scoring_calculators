from shared.calculators.scoring import ConditionalValueEvaluator


class HasAchievedLimitEvaluator(ConditionalValueEvaluator):
    def __init__(self, inclusive_limit: int) -> None:
        super().__init__()
        self.inclusive_limit = inclusive_limit

    def test(self, value):
        return self.inclusive_limit <= value


class HasReached300PassingYardsConditionEvaluator(ConditionalValueEvaluator):
    def test(self, value):
        return 300 <= value


class HasReached100YardsEvaluator(HasAchievedLimitEvaluator):
    def __init__(self) -> None:
        super().__init__(100)


has_reached_100_yards_condition_evaluator = HasReached100YardsEvaluator()

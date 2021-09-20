from daily_fantasy_sports_scoring_calculators.core.calculators.scoring import ConditionEvaluator


class HasAchievedMinimumValueRequirement(ConditionEvaluator):
    def __init__(self, minimum_inclusive_required_value: int) -> None:
        super().__init__()
        self.minimum_inclusive_required_value = minimum_inclusive_required_value

    def test(self, value: int):
        return self.minimum_inclusive_required_value <= value

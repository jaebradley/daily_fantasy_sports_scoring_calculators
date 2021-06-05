from shared.calculators.scoring import StatisticalValueCalculator, PointsCalculator, Rule, RuleValidator


class AlwaysTrueValidator(RuleValidator):
    def test(self, statistics):
        return True


class IdentityValidator(RuleValidator):
    def test(self, value):
        return value


always_true_validator = AlwaysTrueValidator()
identity_validator = IdentityValidator()

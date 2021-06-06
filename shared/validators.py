from shared.calculators.scoring import RuleValidator


class AlwaysTrueValidator(RuleValidator):
    def test(self, statistics):
        return True


class BooleanIdentityValidator(RuleValidator):
    def test(self, value: bool):
        if value is True or value is False:
            return value

        raise ValueError(f'unknown value: {value}')


always_true_validator = AlwaysTrueValidator()
identity_validator = BooleanIdentityValidator()

from shared.calculators.scoring import ConditionalValueEvaluator


class AlwaysTrueValidator(ConditionalValueEvaluator):
    def test(self, statistics):
        return True


class BooleanIdentityValidator(ConditionalValueEvaluator):
    def test(self, value: bool):
        if value is True or value is False:
            return value

        raise ValueError(f'unknown value: {value}')


always_true_validator = AlwaysTrueValidator()
identity_validator = BooleanIdentityValidator()

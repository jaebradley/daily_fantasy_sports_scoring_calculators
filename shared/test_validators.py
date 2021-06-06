from unittest import TestCase
from shared.validators import BooleanIdentityValidator


class TestBooleanIdentityValidator(TestCase):
    def setUp(self) -> None:
        self.instance = BooleanIdentityValidator()

    def test_raises_error_when_non_boolean_value_passed(self):
        with self.assertRaises(ValueError) as error:
            self.instance.test("jaebaebae")

        self.assertEqual(
            "unknown value: jaebaebae",
            str(error.exception)
        )

    def test_returns_true_value(self):
        self.assertTrue(self.instance.test(True))

    def test_returns_false_value(self):
        self.assertFalse(self.instance.test(False))

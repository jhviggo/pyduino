import unittest
import sys
sys.path.append('..')
from validators.PyduinoParameterValidator import PyduinoParameterValidator
from Constants import *


class ParameterValidatorTest(unittest.TestCase):
    def test_positive_parameter_validator_is_digit(self):
        for i in range(0, 10):
            self.assertEqual(PyduinoParameterValidator.is_digit(i), True)
            self.assertEqual(PyduinoParameterValidator.is_digit(str(i)), True)

    def test_negative_parameter_validator_is_digit(self):
        printable_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
        for i in printable_characters:
            self.assertEqual(PyduinoParameterValidator.is_digit(i), False)

        self.assertEqual(PyduinoParameterValidator.is_digit([]), False)
        self.assertEqual(PyduinoParameterValidator.is_digit({}), False)
        self.assertEqual(PyduinoParameterValidator.is_digit(True), False)
        self.assertEqual(PyduinoParameterValidator.is_digit(False), False)

    def test_positive_parameter_validator_pin_mode(self):
        self.assertEqual(PyduinoParameterValidator.validate_pin_modes('o'), True)
        self.assertEqual(PyduinoParameterValidator.validate_pin_modes('O'), True)
        self.assertEqual(PyduinoParameterValidator.validate_pin_modes('P'), True)

        for i in VALID_PIN_MODES.keys():
            self.assertEqual(PyduinoParameterValidator.validate_pin_modes(i), True)

        for i in VALID_PIN_MODES.keys():
            self.assertEqual(PyduinoParameterValidator.validate_pin_modes(i.lower()), True)


    def test_negative_parameter_validator_pin_mode(self):
        self.assertEqual(PyduinoParameterValidator.validate_pin_modes('h'), False)
        self.assertEqual(PyduinoParameterValidator.validate_pin_modes('L'), False)
        self.assertEqual(PyduinoParameterValidator.validate_pin_modes([]), False)
        self.assertEqual(PyduinoParameterValidator.validate_pin_modes({}), False)
        self.assertEqual(PyduinoParameterValidator.validate_pin_modes(True), False)
        self.assertEqual(PyduinoParameterValidator.validate_pin_modes(False), False)

    def test_positive_parameter_validator_digital_range(self):
        self.assertEqual(PyduinoParameterValidator.validate_digital_range(0), True)
        self.assertEqual(PyduinoParameterValidator.validate_digital_range(1), True)
        self.assertEqual(PyduinoParameterValidator.validate_digital_range('HIGH'), True)
        self.assertEqual(PyduinoParameterValidator.validate_digital_range('high'), True)
        self.assertEqual(PyduinoParameterValidator.validate_digital_range('LOW'), True)
        self.assertEqual(PyduinoParameterValidator.validate_digital_range('low'), True)

    def test_negative_parameter_validator_digital_range(self):
        for i in range(-50, 0):
            self.assertEqual(PyduinoParameterValidator.validate_digital_range(i), False)
            self.assertEqual(PyduinoParameterValidator.validate_digital_range(str(i)), False)

        for i in range(2, 50):
            self.assertEqual(PyduinoParameterValidator.validate_digital_range(i), False)
            self.assertEqual(PyduinoParameterValidator.validate_digital_range(str(i)), False)

        self.assertEqual(PyduinoParameterValidator.validate_digital_range([]), False)
        self.assertEqual(PyduinoParameterValidator.validate_digital_range({}), False)
        self.assertEqual(PyduinoParameterValidator.validate_digital_range(False), False)
        self.assertEqual(PyduinoParameterValidator.validate_digital_range(True), False)

    def test_positive_parameter_validator_analog_range(self):
        for i in range(0, 1024):
            self.assertEqual(PyduinoParameterValidator.validate_analog_range(i), True)
            self.assertEqual(PyduinoParameterValidator.validate_analog_range(str(i)), True)

    def test_negative_parameter_validator_analog_range(self):
        for i in range(-50, 0):
            self.assertEqual(PyduinoParameterValidator.validate_analog_range(i), False)

        for i in range(1024, 1100):
                    self.assertEqual(PyduinoParameterValidator.validate_analog_range(i), False)

        self.assertEqual(PyduinoParameterValidator.validate_analog_range([]), False)
        self.assertEqual(PyduinoParameterValidator.validate_analog_range({}), False)
        self.assertEqual(PyduinoParameterValidator.validate_analog_range(True), False)
        self.assertEqual(PyduinoParameterValidator.validate_analog_range(False), False)




import sys
sys.path.append('..')
from Constants import *


class PyduinoParameterValidator:
    @staticmethod
    def is_digit(value):
        if type(value) is int:
            return True

        if type(value) is str:
            if value.isdigit():
                return True
        return False

    @staticmethod
    def validate_pin_modes(pin_mode):
        if type(pin_mode) is not str:
            return False

        if pin_mode.upper() in VALID_PIN_MODES:
            return True
        return False

    @staticmethod
    def validate_digital_range(digital_value):
        if type(digital_value) is str:
            if digital_value.upper() == HIGH or digital_value.upper() == LOW:
                return True

        if not PyduinoParameterValidator.is_digit(digital_value):
            return False

        if DIGITAL_RANGE[0] <= int(digital_value) <= DIGITAL_RANGE[1]:
            return True
        return False

    @staticmethod
    def validate_analog_range(digital_value):
        if not PyduinoParameterValidator.is_digit(digital_value):
            return False

        if ANALOG_RANGE[0] <= int(digital_value) <= ANALOG_RANGE[1]:
            return True
        return False

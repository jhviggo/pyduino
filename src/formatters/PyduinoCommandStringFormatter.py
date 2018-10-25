import sys
sys.path.append('..')
from Constants import *


class PyduinoCommandStringFormatter:
    @staticmethod
    def format_single_pin_mode(pin_number, pin_mode):
        """
        Formats pin mode for single pins

        :param pin_number: int
        :param pin_mode: string
        :return: string
        """
        if type(pin_number) is not int:
            return ''

        if type(pin_mode) is not str:
            return ''

        if pin_mode not in VALID_PIN_MODES.keys():
            return ''

        return str().join((MODE,
                           VALID_PIN_MODES[pin_mode],
                           str(pin_number))).encode()

    @staticmethod
    def format_digital_read(pin_number):
        """
        Formats digital read command

        :param pin_number: int
        :return: string
        """
        if type(pin_number) is not int:
            return ''

        return str().join((READ,
                           DIGITAL,
                           str(pin_number))).encode()

    @staticmethod
    def format_digital_write(pin_number, digital_value):
        """
        Formats digital write command

        :param pin_number: int
        :param digital_value: int
        :return: string
        """
        if type(pin_number) is not int:
            return ''

        if type(digital_value) is not int:
            return ''

        return str().join((WRITE,
                           DIGITAL,
                           str(pin_number),
                           SEPARATOR,
                           str(digital_value))).encode()

    @staticmethod
    def format_analog_read(pin_number):
        """
        Formats analog read command

        :param pin_number: int
        :return: string
        """
        if type(pin_number) is not int:
            return ''

        return str().join((READ,
                           ANALOG,
                           str(pin_number))).encode()

    @staticmethod
    def format_analog_write(pin_number, analog_value):
        """
        Format analog write command

        :param pin_number: int
        :param analog_value: int
        :return: string
        """
        if type(pin_number) is not int:
            return ''

        if type(analog_value) is not int:
            return ''

        return str().join((WRITE,
                           ANALOG,
                           str(pin_number),
                           SEPARATOR,
                           str(analog_value))).encode()

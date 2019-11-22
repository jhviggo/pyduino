from pyduino.HelperFunctions import singleton
from pyduino.formatters.ProtocolStringFormatter import ProtocolStringFormatter
from pyduino.validators.ParameterValidator import ParameterValidator
from pyduino.validators.ProtocolFormatValidator import ProtocolFormatValidator
from pyduino.HelperFunctions import print_verbose


@singleton
class Controller:
    def __init__(self, conn=None, verbose=False):
        self.conn = conn
        self.verbose = verbose
        self.currentActivePins = []

    def set_connection(self, conn):
        """
        Sets the serial connection for the Controller

        :param conn: serial connection from controllers.Connector
        """
        self.conn = conn

    def set_pin_mode(self, pin_number, mode='OUTPUT'):
        """
        Sets a pin with a mode

        :param pin_number:  int
        :param mode: string specified in self.pin_modes
        :return: boolean
        """
        if not ParameterValidator.validate_pin_number(pin_number):
            return False

        if not ParameterValidator.validate_pin_modes(mode):
            return False

        print_verbose('Controller.set_pin_mode.pin.mode')

        try:
            command = ProtocolStringFormatter.format_single_pin_mode(pin_number, mode)
            if not ProtocolFormatValidator.validate_pin_mode(command):
                return False

            print_verbose('Controller.set_pin_mode.pin.mode.as', pin_number, mode, indent=1)
            self.conn.write(command.encode())
            print_verbose('Controller.set_pin_mode.saving.as', pin_number, mode, indent=1)
            self.currentActivePins.append({'pin': pin_number, 'mode': mode})
            return True
        except Exception as e:
            print('\t[-]', e)
            return False

    def set_all_pin_modes(self, pins=()):
        """
        Sets a list of pins with pin modes

        :param pins: tuple of dictionaries
        :return: boolean
        """
        if len(pins) is 0:
            print('\t[-]', 'no pins specified')

        for i in pins:
            if not self.set_pin_mode(i['pin'], i['mode']):
                return False
        return True

    def digital_write(self, pin_number, digital_value):
        """
        Digital write to a pin with data

        :param pin_number: int
        :param digital_value: int
        :return: boolean
        """

        if not ParameterValidator.validate_pin_number(pin_number):
            return False

        if not ParameterValidator.validate_digital_range(digital_value):
            return False

        print_verbose('Controller.digital_write.writing.to')

        try:
            command = ProtocolStringFormatter.format_digital_write(pin_number, digital_value)
            if not ProtocolFormatValidator.validate_write_action(command):
                return False

            print_verbose('Controller.digital_write.writing.to.with', digital_value, pin_number, indent=1)
            self.conn.write(command.encode())
            return True
        except Exception as e:
            print('\t[-]', e)
            return False

    def digital_read(self, pin_number):
        """
        Digital read on a pin

        :param pin_number: int
        :return: int
        """
        if not ParameterValidator.validate_pin_number(pin_number):
            raise RuntimeError('Invalid pin number')

        print_verbose('Controller.digital_read.reading.from')

        try:
            command = ProtocolStringFormatter.format_digital_read(pin_number)
            if not ProtocolFormatValidator.validate_read_action(command):
                raise RuntimeError('Invalid read action format')

            self.conn.write(command.encode())
            print_verbose('Controller.digital_read.reading.from.pin', pin_number, indent=1)
            line_received = self.conn.readline().decode().strip()

            # pyserial may return errors like 'MI8RD8 ERROR' when testing
            # The expected output should contain a ':' like 'D7:1'
            if ':' not in line_received:
                return ''

            header, value = line_received.split(':')
        except Exception as e:
            raise e

        return int(value)

    def analog_write(self, pin_number, analog_value):
        """
        Analog write to a pin with data

        :param pin_number: int
        :param analog_value: int
        :return: boolean
        """
        if not ParameterValidator.validate_pin_number(pin_number):
            return False

        if not ParameterValidator.validate_analog_range(analog_value):
            return False

        print_verbose('Controller.analog_write.writing.to')

        try:
            command = ProtocolStringFormatter.format_analog_write(pin_number, analog_value)
            if not ProtocolFormatValidator.validate_write_action(command):
                return False

            print_verbose('Controller.analog_write.writing.to.pin', analog_value, pin_number, indent=1)
            self.conn.write(command.encode())
            return True
        except Exception as e:
            print('\t[-]', e)
            return False

    def analog_read(self, pin_number):
        """
        Analog read on a pin. Arduino can only return from 0 to 1023

        :param pin_number: int
        :return: boolean
        """
        if not ParameterValidator.validate_pin_number(pin_number):
            return False

        print_verbose('Controller.analog_read.reading.from')

        try:
            command = ProtocolStringFormatter.format_analog_read(pin_number)
            if not ProtocolFormatValidator.validate_read_action(command):
                return False

            self.conn.write(command.encode())
            print_verbose('Controller.analog_read.reading.from.pin', pin_number)
            line_received = self.conn.readline().decode().strip()
            header, value = line_received.split(':')
        except Exception as e:
            print('\t[-]', e)
            return -1

        if header == ('A' + str(pin_number)):
            return int(value)
        return -1

import sys
import time
sys.path.append('..')
from formatters.ProtocolStringFormatter import ProtocolStringFormatter
from validators.ParameterValidator import ParameterValidator
from validators.ProtocolFormatValidator import ProtocolFormatValidator
from HelperFunctions import print_verbose

class Controller:
    def __init__(self, conn, verbose=False):
        self.conn = conn
        self.verbose = verbose
        self.currentActivePins = []


    def get_pulse_in(self):
        self.conn.write("U10".encode())
        return int(self.conn.readline().decode().strip())*0.034/2/1000

    def set_colors(self, R, G, B):
        time.sleep(.1)
        self.toggle_lights('3')
        time.sleep(1)
        print("(" + R + ", " + G + ", " + B + ")")
        self.conn.write(str("PP0;" + R + "." + G + "." + B).encode())

    def toggle_lights(self, status):
        print("[+]lights: " + status) 
        self.conn.write(str('LL' + status).encode())

    def set_led_brightness(self, brightness):
        print("[+]brightness: " + brightness)
        self.conn.write(str('B'+brightness).encode())

    def set_pin_mode(self, pin_number, mode='OUTPUT'):
        """
        sets a pin with a mode

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
            return False

        print_verbose('Controller.digital_read.reading.from')

        try:
            command = ProtocolStringFormatter.format_digital_read(pin_number)
            if not ProtocolFormatValidator.validate_read_action(command):
                return False

            self.conn.write(command.encode())
            print_verbose('Controller.digital_read.reading.from.pin', pin_number, indent=1)
            line_received = self.conn.readline().decode().strip()
            header, value = line_received.split(':')
        except Exception as e:
            print('\t[-]', e)
            return -1

        if header and header == ('D' + str(pin_number)):
            return int(value)
        return -1

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

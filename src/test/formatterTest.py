import unittest
import sys
sys.path.append('..')
from formatters.PyduinoCommandStringFormatter import PyduinoCommandStringFormatter


class TestStringMethods(unittest.TestCase):
    def test_positive_command_formatter_single_pin_mode(self):
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode(5, 'OUTPUT'), 'MO5'.encode())
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode(5, 'O'), 'MO5'.encode())
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode(5, 'INPUT'), 'MI5'.encode())
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode(5, 'I'), 'MI5'.encode())
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode(5, 'INPUT_PULLUP'), 'MP5'.encode())
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode(5, 'P'), 'MP5'.encode())
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode(5, 'P'), 'MP5'.encode())

    def test_negative_command_formatter_single_pin_mode(self):
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode(5, 'testData'), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode(5, ''), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode(5, 12345), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode(5, 12.345), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode(5, True), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode(5, False), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode(5, []), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode(5, ()), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode(5, {}), '')

        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode(5.5, 'O'), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode('5', 'O'), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode('a', 'O'), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode([], 'O'), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode((), 'O'), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode({}, 'O'), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode(True, 'O'), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_single_pin_mode(False, 'O'), '')

    def test_positive_command_formatter_digital_read(self):
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_read(1,), 'RD1'.encode())

    def test_negative_command_formatter_digital_read(self):
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_read('123'), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_read(2.5), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_read(True), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_read(False), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_read([]), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_read(()), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_read({}), '')

    def test_positive_command_formatter_digital_write(self):
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_write(1, 123), 'WD1:123'.encode())

    def test_negative_command_formatter_digital_write(self):
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_write('123', 123), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_write(2.5, 123), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_write(True, 123), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_write(False, 123), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_write([], 123), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_write((), 123), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_write({}, 123), '')

        self.assertEqual(PyduinoCommandStringFormatter.format_digital_write(123, '123'), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_write(123, 2.5), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_write(123, True), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_write(123, False), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_write(123, []), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_write(123, ()), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_digital_write(123, {}), '')

    def test_positive_command_formatter_analog_read(self):
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_read(1), 'RA1'.encode())

    def test_negative_command_formatter_analog_read(self):
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_read('123'), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_read(2.5), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_read(True), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_read(False), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_read([]), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_read(()), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_read({}), '')

    def test_positive_command_formatter_analog_write(self):
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_write(1, 123), 'WA1:123'.encode())

    def test_negative_command_formatter_analog_write(self):
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_write('1', 123), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_write(1.5, 123), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_write(True, 123), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_write(False, 123), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_write([], 123), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_write((), 123), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_write({}, 123), '')

        self.assertEqual(PyduinoCommandStringFormatter.format_analog_write(1, '123'), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_write(1, 2.5), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_write(1, True), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_write(1, False), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_write(1, []), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_write(1, ()), '')
        self.assertEqual(PyduinoCommandStringFormatter.format_analog_write(1, {}), '')


if __name__ == '__main__':
    unittest.main()

import unittest
import sys
sys.path.append('..')
from validators.PyduinoProtocolFormatValidator import PyduinoProtocolFormatValidator

"""
This class assumes the ProtocolStringFormatter validates
the parameters before formatting it, so there is no need
to validate symbols and availability of pins.
"""
class ProtocolFormatValidatorTest(unittest.TestCase):
    def test_positive_protocol_format_validate_pin_mode(self):
        self.assertEqual(PyduinoProtocolFormatValidator.validate_pin_mode('MO5'), True)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_pin_mode('MO71'), True)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_pin_mode('AZ59'), True)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_pin_mode('GI9'), True)

    def test_negative_protocol_format_validate_pin_mode(self):
        self.assertEqual(PyduinoProtocolFormatValidator.validate_pin_mode('M5'), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_pin_mode('M51'), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_pin_mode('GA511'), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_pin_mode('ga11'), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_pin_mode('ok'), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_pin_mode(''), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_pin_mode([]), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_pin_mode({}), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_pin_mode(()), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_pin_mode(True), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_pin_mode(False), False)

    def test_positive_protocol_format_validate_write_action(self):
        self.assertEqual(PyduinoProtocolFormatValidator.validate_write_action('WA1:1'), True)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_write_action('WD1:1'), True)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_write_action('AG11:1'), True)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_write_action('HE1:11'), True)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_write_action('MT11:11'), True)

    def test_negative_protocol_format_validate_write_action(self):
        self.assertEqual(PyduinoProtocolFormatValidator.validate_write_action('W1:1'), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_write_action('Wa1~1'), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_write_action('1:1'), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_write_action('QWE1:1'), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_write_action('QWE1:'), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_write_action('QWE1'), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_write_action('as1:1'), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_write_action('AW1:a'), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_write_action(''), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_write_action([]), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_write_action({}), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_write_action(()), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_write_action(True), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_write_action(False), False)

    def test_positive_protocol_format_validate_read_action(self):
        self.assertEqual(PyduinoProtocolFormatValidator.validate_read_action('RD1'), True)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_read_action('RA1'), True)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_read_action('WA12'), True)

    def test_negative_protocol_format_validate_read_action(self):
        self.assertEqual(PyduinoProtocolFormatValidator.validate_read_action('RD123'), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_read_action('R12'), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_read_action('12AS'), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_read_action('A1'), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_read_action(''), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_read_action([]), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_read_action({}), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_read_action(()), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_read_action(True), False)
        self.assertEqual(PyduinoProtocolFormatValidator.validate_read_action(False), False)



from pyduino.HelperFunctions import HelperFunctions
from pyduino.controllers.Pin import *
import unittest

VERBOSE = True
SERIAL_PORT = 'ttyACM'
READ_TIMEOUT = 1
LANGUAGE = 'en'
options = {
    'verbose': False,
    'language': 'en',
    'env': 'testing'
}


class DigitalPinTest(unittest.TestCase):
    def setUp(self):
        HelperFunctions(options=options)
        connector = Connector(serial_port=SERIAL_PORT, read_timeout=READ_TIMEOUT, verbose=VERBOSE)
        self.conn = connector.get_serial_connection()
        self.controller = Controller(conn=self.conn, verbose=True)

    def test_positive_digital_write(self):
        pin = DigitalPin(self.conn, 8)
        self.assertTrue(pin.write(0))
        self.assertTrue(pin.write(1))

    def test_positive_digital_read(self):
        pin = DigitalPin(self.conn, 8, mode='INPUT')
        self.assertEqual(pin.read(), '')

    def test_raises_digital_read(self):
        pin = DigitalPin(self.conn, 8)
        with self.assertRaises(RuntimeError) as _:
            pin.read()

    def test_raises_digital_write(self):
        pin = DigitalPin(self.conn, 8, mode='INPUT')
        with self.assertRaises(RuntimeError) as _:
            pin.write(1)

    def test_raises_digital_pin_range(self):
        with self.assertRaises(ValueError) as _:
            pin = DigitalPin(self.conn, 14)

    def test_raises_digital_pin_mode(self):
        with self.assertRaises(RuntimeError) as _:
            pin = DigitalPin(self.conn, 8, mode="TEST")

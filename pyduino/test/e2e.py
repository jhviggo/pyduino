from pyduino.controllers.Connector import Connector
from pyduino.controllers.Controller import Controller
from pyduino.HelperFunctions import HelperFunctions

VERBOSE = True
SERIAL_PORT = 'COM3'
READ_TIMEOUT = 1
LANGUAGE = 'en'

if __name__ == '__main__':
    connector = Connector(serial_port=SERIAL_PORT, read_timeout=READ_TIMEOUT, verbose=VERBOSE)
    connector.connect_to_serial_port()
    conn = connector.get_serial_connection()
    options = {
        'serial_port': SERIAL_PORT,
        'read_timeout': READ_TIMEOUT,
        'verbose': VERBOSE,
        'language': LANGUAGE
    }
    HelperFunctions(options=options)

    if conn is None:
        raise Exception('[-] connect_to_serial_port failed')

    controller = Controller(conn, verbose=VERBOSE)

    if not controller.set_pin_mode(5, 'OUTPUT'):
        raise Exception('[-] set_pin_mode failed')

    if not controller.set_all_pin_modes([{"pin": 7, "mode": "INPUT"}, {"pin": 8, "mode": "OUTPUT"}]):
        raise Exception('[-] set_all_pin_modes failed')

    if not controller.digital_write(5, 1):
        raise Exception('[-] digital_write failed')

    if controller.digital_read(5) is not -1:  # Expected to fail
        raise Exception('[-] digital_read did not fail as expected')

    if not controller.analog_write(1, 15):
        raise Exception('[-] analog_write failed')

    if controller.analog_read(1) is not -1:  # Expected to fail
        raise Exception('[-] analog_read did not fail as expected')

    if not connector.close_connection():
        raise Exception('[-] close_connection failed')

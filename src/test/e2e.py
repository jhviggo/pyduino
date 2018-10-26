import sys
sys.path.append('..')
from controllers.Connector import Connector
from controllers.Controller import Controller

if __name__ == '__main__':
    connector = Connector(serial_port='COM3', read_timeout=1, verbose=True)
    conn = connector.connect_to_serial_port()
    if conn is None:
        raise Exception('[-] connect_to_serial_port failed')

    controller = Controller(conn, verbose=True)

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

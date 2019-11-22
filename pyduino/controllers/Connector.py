import serial
from pyduino.HelperFunctions import singleton


@singleton
class Connector:
    def __init__(self, serial_port='COM6', baud_rate=9600, read_timeout=5, verbose=False):
        self.conn = None
        self.serial_port = serial_port
        self.read_timeout = read_timeout
        self.baud_rate = baud_rate
        self.verbose = verbose

        self.connect_to_serial_port()

    def get_connection(self) -> serial:
        return self.conn

    def connect_to_serial_port(self):
        """
        Connects to a serial port COM2, COM3, COM6 TTY...

        :return: Serial object
        """
        if self.verbose:
            print('Connecting to port [' + self.serial_port + ']...', end='')
        try:
            self.conn = serial.Serial(self.serial_port, self.baud_rate)
            self.conn.timeout = self.read_timeout
            if self.verbose:
                print('Connected')
            return True
        except Exception as e:
            print('\n\t[-]', e)
            return False

    def get_serial_connection(self):
        return self.conn

    def close_connection(self):
        """
        Close connection to serial port

        :return: boolean
        """
        if self.verbose:
            print('Closing connection...', end='')
        try:
            self.conn.close()
            if self.verbose:
                print('Closed')
            return True
        except Exception as e:
            print('\n\t[-]', e)
            return False

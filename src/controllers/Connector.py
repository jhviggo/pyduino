import serial


class Connector:
    def __init__(self, serial_port='COM6', baud_rate=9600, read_timeout=5, verbose=False):
        self.conn = None
        self.serial_port = serial_port
        self.read_timeout = read_timeout
        self.baud_rate = baud_rate
        self.verbose = verbose

    def connect_to_serial_port(self):
        """
        Connects to a serial port COM2, COM3, COM6 TTY...

        :return: Serial object
        """
        if self.verbose:
            print('Connecting to port', self.serial_port + '...')
        try:
            self.conn = serial.Serial(self.serial_port, self.baud_rate)
            self.conn.timeout = self.read_timeout
            return self.conn
        except Exception as e:
            print('\t[-]', e)
            return None

    def close_connection(self):
        """
        Close connection to serial port

        :return: boolean
        """
        if self.verbose:
            print('Closing connection...')
        try:
            self.conn.close()
            if self.verbose:
                print('\t', 'connection closed')
            return True
        except Exception as e:
            print('\t[-]', e)
            return False

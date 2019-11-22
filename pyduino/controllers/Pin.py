from pyduino.Constants import OUTPUT, INPUT
from pyduino.controllers.Connector import Connector
from pyduino.controllers.Controller import Controller
from pyduino.validators.ParameterValidator import ParameterValidator


class PinInterface:
    def __init__(self):
        if Connector().conn is None:
            raise RuntimeError("[-] No serial connection found")

        if Controller().conn is None:
            print("[!] Controller not initialized")
            print("\tInitialize Controller...")
            Controller().set_connection(Connector().get_connection())

    def write(self, value) -> bool:
        raise NotImplementedError("[-] Write not implemented")

    def read(self) -> bool:
        raise NotImplementedError("[-] Read not implemented")


class DigitalPin(PinInterface):
    conn: Connector = None
    pin_number: int = -1
    mode: str = None

    def __init__(self, conn: Connector, pin_number: int, mode: str = OUTPUT):
        PinInterface.__init__(self)

        if not ParameterValidator.validate_pin_number(pin_number):
            raise ValueError("pin_number must be a valid digital pin")

        if not Controller().set_pin_mode(pin_number, mode=mode):
            raise Exception("Failed to set pin " + str(pin_number) + " to " + mode)

        self.conn = conn
        self.pin_number = pin_number
        self.mode = mode

    def write(self, value) -> bool:
        """
        Writes to the digital port

        :param value: The value to be written. Must be HIGH or LOW
        :type value: int
        :raises RuntimeError: Cannot write to INPUT ports
        """
        if self.mode == INPUT:
            raise RuntimeError("[-] Cannot write to an INPUT port")

        return Controller().digital_write(self.pin_number, value)

    def read(self) -> bool:
        """
        Reads from the digital port

        :raises RuntimeError: Cannot read from OUTPUT ports
        """
        if self.mode == OUTPUT:
            raise RuntimeError("[-] Cannot read from an OUTPUT port")

        return Controller().digital_read(self.pin_number)

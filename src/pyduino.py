import serial
import time

class Arduino():
    def __init__(self, perm_pin=None, serial_port='COM6', baud_rate=9600, read_timeout=5):
        self.conn = serial.Serial(serial_port, baud_rate)
        self.conn.timeout = read_timeout
        self.perm_pin = perm_pin
        self.fire_pin = 13

    def set_pin_mode(self, pin_number, mode='O'):
        """
        - I for INPUT
        - O for OUTPUT
        - P for INPUT_PULLUP MO13
        """
        command = (''.join(('M',mode, str(pin_number)))).encode()
        self.conn.write(command)

    def set(self, new_mode='O'):
        command = (''.join(('M',new_mode,str(self.perm_pin)))).encode()
        self.conn.write(command)

    def change_pin(self, new_pin):
        self.perm_pin = new_pin

    def change_fire_pin(self, new_pin):
        self.fire_pin = new_pin

    def on(self):
        self.digital_write(self.perm_pin, 1)

    def on_for(self, sec):
        self.digital_write(self.fire_pin, 1)
        now = time.time()
        while True:
            if time.time() - now > sec:
                print("%.3f" % float(time.time() - now))
                break
        self.digital_write(self.fire_pin, 0)

    def on_off(self, ticks, t=1):
        for i in range(ticks):
            self.digital_write(self.fire_pin, 1)
            time.sleep(t)
            self.digital_write(self.fire_pin, 0)
            time.sleep(t)

    def off(self):
        self.digital_write(self.perm_pin, 0)

    def digital_read(self, pin_number):
        command = (''.join(('RD', str(pin_number)))).encode()
        self.conn.write(command)
        line_received = self.conn.readline().decode().strip()
        header, value = line_received.split(':')
        if header == ('D'+ str(pin_number)):
            return int(value)

    def digital_write(self, pin_number, digital_value):
        command = (''.join(('WD', str(pin_number), ':',
            str(digital_value)))).encode()
        self.conn.write(command)

    def analog_read(self, pin_number):
        command = (''.join(('RA', str(pin_number)))).encode()
        self.conn.write(command)
        line_received = self.conn.readline().decode().strip()
        header, value = line_received.split(':')
        if header == ('A'+ str(pin_number)):
            return int(value)

    def analog_write(self, pin_number, analog_value):
        command = (''.join(('WA', str(pin_number), ':',
            str(analog_value)))).encode()
        self.conn.write(command)

    def close(self):
        self.conn.close()
        print('Connection to Arduino closed')

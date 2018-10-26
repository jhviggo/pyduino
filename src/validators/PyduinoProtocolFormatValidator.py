import re


class PyduinoProtocolFormatValidator:
    @staticmethod
    def validate_pin_mode(command):
        if type(command) is not str:
            return False

        if not re.match('^[A-Z]{2}\d{1,2}$', command):
            return False
        return True

    @staticmethod
    def validate_write_action(command):
        if type(command) is not str:
            return False

        if not re.match('^[A-Z]{2}\d{1,2}:\d{1,4}$', command):
            return False
        return True

    @staticmethod
    def validate_read_action(command):
        if type(command) is not str:
            return False

        if not re.match('^[A-Z]{2}\d{1,2}$', command):
            return False
        return True

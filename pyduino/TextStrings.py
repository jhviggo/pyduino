""""
Naming convention:

    Class.method_name.description: {
        da,
        en,
        ?other
    }

"""

TEXT_STRINGS = {
    'Controller.set_pin_mode.pin.mode': {
        'da': 'Sætter pin tilstand',
        'en': 'Setting pin mode'
    },
    'Controller.set_pin_mode.pin.mode.as': {
        'da': 'Sætter pin {} som {}',
        'en': 'Setting pin {} as {}'
    },
    'Controller.set_pin_mode.saving.as': {
        'da': 'Gemmer som {{ "pin": {}, "mode": "{}" }} til hukommelse',
        'en': 'Saving as {{ "pin": {}, "mode": "{}" }} to memory'
    },
    'Controller.digital_write.writing.to': {
        'da': 'Skriver til digital pin',
        'en': 'Writing to digital pin'
    },
    'Controller.digital_write.writing.to.with': {
        'da': 'Skriver {} til digital pin {}',
        'en': 'Writing {} to digital pin {}'
    },
    'Controller.digital_read.reading.from': {
        'da': 'Læser fra digital pin',
        'en': 'Reading from digital pin'
    },
    'Controller.digital_read.reading.from.pin': {
        'da': 'Læser fra digital pin {}',
        'en': 'reading from digital pin {}'
    },
    'Controller.analog_write.writing.to': {
        'da': 'Skriver til analog pin',
        'en': 'Writing to analog pin'
    },
    'Controller.analog_write.writing.to.pin': {
        'da': 'Skriver {} til analog pin {}',
        'en': 'Writing {} to analog pin {}'
    },
    'Controller.analog_read.reading.from': {
        'da': 'Læser fra analog pin',
        'en': 'Reading from analog pin'
    },
    'Controller.analog_read.reading.from.pin': {
        'da': 'Læser fra analog pin {}',
        'en': 'Reading from analog pin {}'
    }
}


def get_language_text(text, *args, lang='en'):
    if text in TEXT_STRINGS:
        return TEXT_STRINGS[text][lang].format(*args)
    return ''

from TextStrings import get_language_text


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class HelperFunctions:
    def __init__(self, options=None):
        self.options = options

    def get_verbose(self):
        return self.options['verbose']

    def get_options(self):
        return self.options


def print_verbose(text, *args, indent=0):
    if HelperFunctions().get_options()['verbose']:
        print('\t'*indent, end='')
        print(get_language_text(text, *args, lang=HelperFunctions().get_options()['language']))

from pyduino import Arduino
import win32api
import time
import sys

a = Arduino(perm_pin=10)

# a.set() in shell


def close():
    a.close()
    sys.exit(1)

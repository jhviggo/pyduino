from controllers.Connector import Connector
from HelperFunctions import HelperFunctions
from controllers.Controller import Controller
import time
import threading

VERBOSE = True
SERIAL_PORT = '/dev/ttyACM1'
READ_TIMEOUT = 1
LANGUAGE = 'en'
connector = None
conn = None
controller = None

options = {
    'serial_port': SERIAL_PORT,
    'read_timeout': READ_TIMEOUT,
    'verbose': VERBOSE,
    'language': LANGUAGE
}
HelperFunctions(options=options)


hasBeenInitialized = False
lightsAreOn = False
ledBrightness = 255;

def check_motion():
    while true:
        print(".")
        if controller.get_pulse_in():
            controller.toggle_lights(1)
            print("YES")

threading.Thread(target=check_motion)


import falcon

class InitPy:
    def on_get(self, req, resp):
        global connector, conn, controller, HelperFunction, hasBeenInitialized
        if hasBeenInitialized:
            resp.media = 'App has already been initialized'
            return

        connector = Connector(serial_port=SERIAL_PORT, read_timeout=READ_TIMEOUT, verbose=VERBOSE)
        connector.connect_to_serial_port()
        conn = connector.get_serial_connection()
        controller = Controller(conn, verbose=VERBOSE)  
        controller.set_pin_mode(7)
        controller.set_pin_mode(13)
        hasBeenInitialized = True
        resp.media = "Initialized!"

class PinAction:
    def on_post(self, req, resp, con, action, pin, value):
        if not hasBeenInitialized:
            resp.media = 'App has not been initialized'
            return

        if con.lower() == 'digital':
            print(pin, value)
            resp.media = controller.digital_write(int(pin), int(value))
        elif con.lower() == 'analog':
            resp.media = controller.analog_write(int(pin), int(value))
        else:
            resp.media = 'ERROR'
            resp.status = falcon.HTTP_400

    def on_get(self, req, resp, con, action, pin, value):
        if not hasBeenInitialized:
            resp.media = 'App has not been initialized'
            return

        if con.lower() == 'digital':
            resp.media = controller.digital_read(int(pin))
        elif con.lower() == 'analog':
            resp.media = controller.analog_read(int(pin))
        else:
            resp.media = 'ERROR'
            resp.status = falcon.HTTP_400;

class PulseIn:
    def on_get(self, req, resp):
        distance = controller.get_pulse_in()
        resp.media = distance

class Lights:
    def on_post(self, req, resp, status):
        global lightsAreOn

        if int(status) == 1:
            ligthsAreOn = True
        elif int(status) == 0:
            lightAreOn = False

        controller.toggle_lights(status)
        resp.media = lightsAreOn

class Information:
    def on_get(self, req, resp):
        resp.media = {
            'lights': lightsAreOn,
            'init': hasBeenInitialized,
            'distance': controller.get_pulse_in(),
            'motion': controller.digital_read(int(2)),
            'brightness': ledBrightness
        }

class Brightness:
    def on_post(self, req, resp, brightness):
        global ledBrightness

        controller.set_led_brightness(brightness)
        ledBrightness = brightness

class PredefinedColors:
    def on_post(self, req, resp, R, G, B):
        controller.set_colors(R, G, B)
        resp.media = "(" + R + ", " + G + ", " + B + ")"

api = falcon.API()
api.add_route('/init', InitPy())
api.add_route('/{con}/{action}/{pin}/{value}', PinAction())
api.add_route('/pulsein', PulseIn())
api.add_route('/lights/{status}', Lights())
api.add_route('/info', Information())
api.add_route('/brightness/{brightness}', Brightness())
api.add_route('/colors/{R}/{G}/{B}', PredefinedColors())

if connector != None:
    connector.close_connection()

import win32api
import sys
import time
import os
from math import sqrt
from pyduino import Arduino

SPACE = 32
LEFT_ARROW = 37
RIGHT_ARROW = 39
C = 67
C_UP = False
Q = 81
R = 82
R_UP = False
T = 84
T_UP = False
LOW = 0
HIGH = 1
RIGHT = LOW
LEFT = HIGH
STEPS = 4000.0
DEGREES_IN_CIRCLE = 360.0
FIRE_TIME = 0.5
STEP_ANGLE = 1
REVERSE = -1
FIRE_OFF = True
TIMER = 0
ENABLE = "ENABLED"

class Stepper:
    def __init__(self, arduino, perm_pin=10, fire_pin=13):
        self.arduino = arduino
        self.arduino.set_pin_mode(perm_pin)
        self.arduino.set_pin_mode(fire_pin)
        self.perm_pin = perm_pin
        self.direction = 0

    def step(self):
        self.arduino.on()
        self.arduino.off()

    def FIRE(self):
        print "FIRE!!"
        self.arduino.on_for(FIRE_TIME)

    def step_for(self,t):
        for i in xrange(t):
            self.arduino.on()
            self.arduino.off()

            if win32api.GetAsyncKeyState(Q):
                print "Stepped " + i + " times."
                break

    def step_degree(self, degrees):
        degree = STEPS/DEGREES_IN_CIRCLE

        if degrees < 0 and self.direction is RIGHT:
            self.switch()

        for i in xrange(abs(int(degree*degrees))):
            self.arduino.on()
            self.arduino.off()

            if win32api.GetAsyncKeyState(Q):
                print "Stepped " + str(i) + " times.\n" + str(i/degree) + " degrees"
                self.arduino.off()
                break
            
        if self.direction is LEFT:
            self.switch()

    def switch(self):
        if self.direction is RIGHT:
            self.direction = LEFT
            self.arduino.digital_write(self.perm_pin, HIGH)
        elif self.direction is LEFT:
            self.direction = RIGHT
            self.arduino.digital_write(self.perm_pin ,LOW)
        else:
            print "What the fuck did you do?"

    def step_control(self):
        global FIRE_OFF, TIMER, T_UP, R_UP, ENABLE
        while True:
            # Clears screen
            if win32api.GetAsyncKeyState(C):
                if not C_UP:
                    desc()
                C_UP = True
            else:
                C_UP = False
            
            # Enable/Disable FIRE
            if win32api.GetAsyncKeyState(R):
                if not R_UP:
                    if FIRE_OFF is True:
                        ENABLE = "DISABLED"
                        desc()
                        FIRE_OFF = False
                    elif FIRE_OFF is False:
                        ENABLE = "ENABLED"
                        FIRE_OFF = True
                        desc()
                    else:
                        print "Wat?"
                    R_UP = True
            else:
                if R_UP:
                    R_UP =  False

            # Main controlls, arrowkeys and space
            if win32api.GetAsyncKeyState(SPACE) and FIRE_OFF:
                self.FIRE()
            elif win32api.GetAsyncKeyState(RIGHT_ARROW):
                if self.direction is LEFT:
                    self.switch()
                self.step_degree(STEP_ANGLE)
            elif win32api.GetAsyncKeyState(LEFT_ARROW):
                if self.direction is RIGHT:
                    self.switch()
                self.step_degree(STEP_ANGLE * REVERSE)

            # Makes a timer
            if win32api.GetAsyncKeyState(T):
                if not T_UP:
                    if TIMER is 0:
                        print "Timer started: ",
                        TIMER = time.time()
                    elif TIMER is not 0:
                        print str(time.time() - TIMER) + "Sec"
                        TIMER = 0
                T_UP = True
            else:
                T_UP = False
                 
            # Quit the controller
            if win32api.GetAsyncKeyState(Q):
                if self.direction is LEFT:
                    self.switch()
                    self.close()
                break
            
    def close(self):
        self.arduino.digital_write(self.perm_pin, LOW)
        self.arduino.off()
        self.arduino.close()

def desc():
    os.system("cls")
    print "---| Interactive prompt is now active |---"
    print "T\t-\tStart and stop timer."
    print "R\t-\tEnable or Disable FIRE."
    print "Q\t-\tQuit."
    print "C\t-\tClear."
    print "Right\t-\tTurns right."
    print "Left\t-\tTurns right." 
    print "Space\t-\tFIRE!"
    print "------------------------------------------"
    print ENABLE

def main():
    raw_input("WARNING!! Arduino will FIRE!!\nPress Enter...")
    print "[+] Connecting to Arduino..."
    s = None
    try:
        a = Arduino()
    except:
        print "[-] Unable to connect to Arduino, please check connection"
        os.system("pause")
    a.change_pin(9)
    time.sleep(1)
    print "[+] Setting default pins..."
    a.set() # me plox
    time.sleep(1)
    print "[+] Setting pin 13 for FIRE..."
    a.set_pin_mode(13)
    time.sleep(1)
    print "[+] Activating interactive prompt..."
    s = Stepper(a)
    time.sleep(1)
    desc()
    s.step_control()
    
main()
os.system("cls")
sys.exit(1)
   

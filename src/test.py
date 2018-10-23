import stepper
import pyduino
a = pyduino.Arduino()
a.change_pin(9)
a.set()
#a.set_pin_mode(13)
s = stepper.Stepper(a)
s.step_control()

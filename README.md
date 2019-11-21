# Pyduino project
This is a school project originally based on [lekum/pyduino](https://github.com/lekum/pyduino) and has evolved a lot from his original code.

It allows you to set pins as `OUTPUT` or `INPUT` and read/write to either digital or analog pins. It is a way to work with the Arduino without having to code C++ and compile it every time. With this library you can interactively set, read from and write to pins.

## Supports Python Versions
```
Python v3.x
```

## Setup
The project will work for both Mac, Linux and Windows.

### Install
```bash
# Clone project
git clone git@github.com:jhviggo/pyduino.git
cd pyduino

# Install pyduino package
pip install -r requirements.txt
pip install . # Installs pyduino package
```

### Arduino setup

Compile the file `src/arduino/pyduino.ino` to your arduino, it contains the protocol used to communicate with it. Make sure it compiles correctly and try running:
```bash
python pyduino/test/e2e.py
```
You should see output somewhat like this:
```
Connecting to port COM3...
Setting pin mode
         setting pin 5 as OUTPUT
         saving as {"pin": 5, "mode": "OUTPUT"} to local storage
Setting pin mode
         setting pin 7 as INPUT
         saving as {"pin": 7, "mode": "INPUT"} to local storage
Setting pin mode
         setting pin 8 as OUTPUT
         saving as {"pin": 8, "mode": "OUTPUT"} to local storage
Writing to digital pin
         writing 1 to digital pin 5
Reading from digital pin
         reading from digital pin 5
        [-] not enough values to unpack (expected 2, got 1)
Writing to analog pin
         writing 15 to analog pin 1
Reading from analog pin
         reading from analog pin 1
        [-] not enough values to unpack (expected 2, got 1)
Closing connection...
         connection closed
```

### run
Currently there is no CLI or interactive interface. You will have to import the controllers from a python terminal.
```bash
# find project source
cd pyduino/src

python
```
```python
# import Connector and controller
from pyduino.controllers import Connector
from pyduino.controllers import Controller

# create an instance with serial_port and if you want verbose prints
connector = Connector(serial_port='COM3', read_timeout=1, verbose=True)
conn = connector.connect_to_serial_port()

# pass the connection to the controller
controller = Controller(conn, verbose=True)

# set pin_mode and write
controller.set_pin_mode(7, 'OUTPUT')
controller.digital_write(7, 1)

# set pin_mode and read
controller.set_pin_mode(8, 'INPUT')
controller.digital_read(8)

# close connection
connector.close_connection()
```

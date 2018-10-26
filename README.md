# Pyduino project
This project is a python controller for Arduino.

It allows you to set pins as `OUTPUT` or `INPUT` and read/write to either digital or analog pins. It is a way to work with the Arduino without having to code C++ and compile it every time. With this library you can interactively set, read from and write to pins.

## Versions
```
Python v3.5
```

## Setup
The project will work for both Mac, Linux and Windows.
### install
Install instruction for linux.
```bash
# install Python35 or newer and pip3
sudo apt install python3.5
sudo apt install python3-pip

# install pySerial library
pip3 install pyserial

# clone project
git clone git@github.com:jhviggo/pyduino.git
```

### run
Currently there is no CLI or interactive interface. You will have to import the controllers from a python terminal.
```bash
# find project source
cd pyduino/src

# open python 3.5 or higher
python3
```
```python
# import Connector and controller
import controllers.PyduinoConnector
import controllers.PyduinoController

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
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
```
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
```
# import project
cd pyduino/src

python3
> import controllers.PyduinoConnector
> import controllers.PyduinoController
```
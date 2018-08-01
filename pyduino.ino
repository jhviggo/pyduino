char operation;
char mode;
int pin_number;
int digital_value; 
int analog_value;
int value_to_write;
int wait_for_transmission = 5;

void set_pin_mode(int pin_number, char mode){
    /*
     * - I: Sets the mode to INPUT
     * - O: Sets the mode to OUTPUT
     * - P: Sets the mode to INPUT_PULLUP
     */

    switch (mode){
        case 'I':
            pinMode(pin_number, INPUT);
            break;
        case 'O':
            pinMode(pin_number, OUTPUT);
            break;
        case 'P':
            pinMode(pin_number, INPUT_PULLUP);
            break;
    } 
}

void digital_read(int pin_number){
    digital_value = digitalRead(pin_number);
    Serial.print('D');
    Serial.print(pin_number);
    Serial.print(':');
    Serial.println(digital_value);
}

void analog_read(int pin_number){
    analog_value = analogRead(pin_number);
    Serial.print('A');
    Serial.print(pin_number);
    Serial.print(':');
    Serial.println(analog_value);
}

void digital_write(int pin_number, int digital_value){
  digitalWrite(pin_number, digital_value);
}

void analog_write(int pin_number, int analog_value){
  analogWrite(pin_number, analog_value);
}

void setup() {
    Serial.begin(9600);
    Serial.setTimeout(100);
}

void loop() {
    if (Serial.available() > 0) {
        operation = Serial.read();
        delay(wait_for_transmission);
        mode = Serial.read();
        pin_number = Serial.parseInt();
        if (Serial.read()==':'){
            value_to_write = Serial.parseInt();
        }
        switch (operation){
            case 'R':
                if (mode == 'D'){
                    digital_read(pin_number);
                } else if (mode == 'A'){
                    analog_read(pin_number);
        } else {
          break;
        }
                break;

            case 'W':
                if (mode == 'D'){
                    digital_write(pin_number, value_to_write);
                } else if (mode == 'A'){
                    analog_write(pin_number, value_to_write);
                } else {
                    break;
                }
                break;

            case 'M':
                set_pin_mode(pin_number, mode);
                break;

            default:
                break;
        }
    }
}

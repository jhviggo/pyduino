#include <FastLED.h>

#define NUM_LEDS 123
#define DATA_PIN 7

#define NOTE_B0  31
#define NOTE_C1  33
#define NOTE_CS1 35
#define NOTE_D1  37
#define NOTE_DS1 39
#define NOTE_E1  41
#define NOTE_F1  44
#define NOTE_FS1 46
#define NOTE_G1  49
#define NOTE_GS1 52
#define NOTE_A1  55
#define NOTE_AS1 58
#define NOTE_B1  62
#define NOTE_C2  65
#define NOTE_CS2 69
#define NOTE_D2  73
#define NOTE_DS2 78
#define NOTE_E2  82
#define NOTE_F2  87
#define NOTE_FS2 93
#define NOTE_G2  98
#define NOTE_GS2 104
#define NOTE_A2  110
#define NOTE_AS2 117
#define NOTE_B2  123
#define NOTE_C3  131
#define NOTE_CS3 139
#define NOTE_D3  147
#define NOTE_DS3 156
#define NOTE_E3  165
#define NOTE_F3  175
#define NOTE_FS3 185
#define NOTE_G3  196
#define NOTE_GS3 208
#define NOTE_A3  220
#define NOTE_AS3 233
#define NOTE_B3  247
#define NOTE_C4  262
#define NOTE_CS4 277
#define NOTE_D4  294
#define NOTE_DS4 311
#define NOTE_E4  330
#define NOTE_F4  349
#define NOTE_FS4 370
#define NOTE_G4  392
#define NOTE_GS4 415
#define NOTE_A4  440
#define NOTE_AS4 466
#define NOTE_B4  494
#define NOTE_C5  523
#define NOTE_CS5 554
#define NOTE_D5  587
#define NOTE_DS5 622
#define NOTE_E5  659
#define NOTE_F5  698
#define NOTE_FS5 740
#define NOTE_G5  784
#define NOTE_GS5 831
#define NOTE_A5  880
#define NOTE_AS5 932
#define NOTE_B5  988
#define NOTE_C6  1047
#define NOTE_CS6 1109
#define NOTE_D6  1175
#define NOTE_DS6 1245
#define NOTE_E6  1319
#define NOTE_F6  1397
#define NOTE_FS6 1480
#define NOTE_G6  1568
#define NOTE_GS6 1661
#define NOTE_A6  1760
#define NOTE_AS6 1865
#define NOTE_B6  1976
#define NOTE_C7  2093
#define NOTE_CS7 2217
#define NOTE_D7  2349
#define NOTE_DS7 2489
#define NOTE_E7  2637
#define NOTE_F7  2794
#define NOTE_FS7 2960
#define NOTE_G7  3136
#define NOTE_GS7 3322
#define NOTE_A7  3520
#define NOTE_AS7 3729
#define NOTE_B7  3951
#define NOTE_C8  4186
#define NOTE_CS8 4435
#define NOTE_D8  4699
#define NOTE_DS8 4978
#define REST      0

// change this to make the song slower or faster
int tempo = 160;

// change this to whichever pin you want to use
int buzzer = 8;

int melody[] = {

  // We Wish You a Merry Christmas
  // Score available at https://musescore.com/user/6208766/scores/1497501
  
  NOTE_C5,4, //1
  NOTE_F5,4, NOTE_F5,8, NOTE_G5,8, NOTE_F5,8, NOTE_E5,8,
  NOTE_D5,4, NOTE_D5,4, NOTE_D5,4,
  NOTE_G5,4, NOTE_G5,8, NOTE_A5,8, NOTE_G5,8, NOTE_F5,8,
  NOTE_E5,4, NOTE_C5,4, NOTE_C5,4,
  NOTE_A5,4, NOTE_A5,8, NOTE_AS5,8, NOTE_A5,8, NOTE_G5,8,
  NOTE_F5,4, NOTE_D5,4, NOTE_C5,8, NOTE_C5,8,
  NOTE_D5,4, NOTE_G5,4, NOTE_E5,4,

  NOTE_F5,2, NOTE_C5,4, //8 
  NOTE_F5,4, NOTE_F5,8, NOTE_G5,8, NOTE_F5,8, NOTE_E5,8,
  NOTE_D5,4, NOTE_D5,4, NOTE_D5,4,
  NOTE_G5,4, NOTE_G5,8, NOTE_A5,8, NOTE_G5,8, NOTE_F5,8,
  NOTE_E5,4, NOTE_C5,4, NOTE_C5,4,
  NOTE_A5,4, NOTE_A5,8, NOTE_AS5,8, NOTE_A5,8, NOTE_G5,8,
  NOTE_F5,4, NOTE_D5,4, NOTE_C5,8, NOTE_C5,8,
  NOTE_D5,4, NOTE_G5,4, NOTE_E5,4,
  NOTE_F5,2, NOTE_C5,4,

  NOTE_F5,4, NOTE_F5,4, NOTE_F5,4,//17
  NOTE_E5,2, NOTE_E5,4,
  NOTE_F5,4, NOTE_E5,4, NOTE_D5,4,
  NOTE_C5,2, NOTE_A5,4,
  NOTE_AS5,4, NOTE_A5,4, NOTE_G5,4,
  NOTE_C6,4, NOTE_C5,4, NOTE_C5,8, NOTE_C5,8,
  NOTE_D5,4, NOTE_G5,4, NOTE_E5,4,
  NOTE_F5,2, NOTE_C5,4, 
  NOTE_F5,4, NOTE_F5,8, NOTE_G5,8, NOTE_F5,8, NOTE_E5,8,
  NOTE_D5,4, NOTE_D5,4, NOTE_D5,4,
  
  NOTE_G5,4, NOTE_G5,8, NOTE_A5,8, NOTE_G5,8, NOTE_F5,8, //27
  NOTE_E5,4, NOTE_C5,4, NOTE_C5,4,
  NOTE_A5,4, NOTE_A5,8, NOTE_AS5,8, NOTE_A5,8, NOTE_G5,8,
  NOTE_F5,4, NOTE_D5,4, NOTE_C5,8, NOTE_C5,8,
  NOTE_D5,4, NOTE_G5,4, NOTE_E5,4,
  NOTE_F5,2, NOTE_C5,4,
  NOTE_F5,4, NOTE_F5,4, NOTE_F5,4,
  NOTE_E5,2, NOTE_E5,4,
  NOTE_F5,4, NOTE_E5,4, NOTE_D5,4,
};

int notes = sizeof(melody) / sizeof(melody[0]) / 2;

// this calculates the duration of a whole note in ms
int wholenote = (60000 * 4) / tempo;

int divider = 0, noteDuration = 0;

int noteCounter = 0;

const int trigPin = 9;
const int echoPin = 10;

char operation;
char mode;
int pin_number;
int digital_value; 
int analog_value;
int value_to_write;
int wait_for_transmission = 5;
boolean lightAreOn = false;
int light_mode = 2; // 1 = blinking, 2 = static, 3 = predefined

int red = 255;
int green = 255;
int blue = 255;


long duration;

CRGB leds[NUM_LEDS];
long randNumber;
long randNumber2;
long randNumber3;
long randNumber4;

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

void get_duration() {
  Serial.print(duration);
}

void set_led_brightness(int brightness) {
  LEDS.setBrightness(brightness);
}

void run_lights() {
  for(int i = 0; i < NUM_LEDS; i++) {
      randNumber = random(0, NUM_LEDS);
      randNumber2 = random(0, 255);
      randNumber3 = random(0, 255);
      randNumber4 = random(0, 255);

      leds[randNumber].setRGB(randNumber2, randNumber3, randNumber4);
      leds[i] = CRGB::Black;
    }

    FastLED.show();

    if (noteCounter < notes*2) {
      divider = melody[noteCounter + 1];
      if (divider > 0) {
        noteDuration = (wholenote) / divider;
      } else if (divider < 0) {
        noteDuration = (wholenote) / abs(divider);
        noteDuration *= 1.5; // increases the duration in half for dotted notes
      }
      tone(buzzer, melody[noteCounter], noteDuration * 0.9);
      delay(noteDuration/2);
      noTone(buzzer);
      noteCounter += 2;
    }
}

void static_lights() {
    for(int i = 0; i < NUM_LEDS; i++) {
      if (i%3 == 0) {
        leds[i].setRGB(255, 0, 0);
      } else if (i%3 == 2) {
        leds[i].setRGB(0, 255, 0);
      } else {
        leds[i].setRGB(0, 0, 255);
      }
    }
    FastLED.show();
}

void defined_lights() {
    for(int i = 0; i < NUM_LEDS; i++) {
      leds[i].setRGB(green, red, blue);
    }
    FastLED.show();
}

void stop_lights() {
  lightAreOn = false;

  for(int i = 0; i < NUM_LEDS; i++) {
      leds[i].setRGB(0,0,0);
    }
    FastLED.show();
}

void start_lights() {
  lightAreOn = true;
}

void setup() {
    Serial.begin(9600);
    Serial.setTimeout(100);
    pinMode(9, OUTPUT);
    pinMode(10, INPUT);
    pinMode(13, OUTPUT);
    pinMode(2, INPUT);
    FastLED.addLeds<WS2812B, DATA_PIN, RGB>(leds, NUM_LEDS);
    randomSeed(analogRead(0));
    LEDS.setBrightness(255);
    stop_lights();
}

void loop() {
    // check for motion
    if (digitalRead(2) == HIGH) {
        digitalWrite(13, HIGH);
        lightAreOn = true;
    } else {
      digitalWrite(13, LOW);
    }
  
    // update ultrasonic sensor
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    duration = pulseIn(echoPin, HIGH);


    // Lights
    if (lightAreOn) {
      if (light_mode == 1) {
        run_lights();
      }
      else if (light_mode == 2) {
        static_lights();
      }
      else if (light_mode == 3) {
        defined_lights();
      }
    }
  
    if (Serial.available() > 0) {
        operation = Serial.read();
        delay(wait_for_transmission);
        mode = Serial.read();
        pin_number = Serial.parseInt();

        int temp = Serial.read();
        if (temp==':'){
            value_to_write = Serial.parseInt();
        } else if (temp == ';') {
          red = Serial.parseInt();
          Serial.print(red);
          Serial.read();
          green = Serial.parseInt();
          Serial.print(green);
          Serial.read();
          blue = Serial.parseInt();
          Serial.print(blue);
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
            case 'U':
                get_duration();
                Serial.print(duration);
                break;
            case 'L':
                if (pin_number == 3) {
                  defined_lights();
                  light_mode = 3;
                } else if (pin_number == 2){
                  start_lights();
                  light_mode = 2;
                } else if (pin_number == 1) {
                  start_lights();
                  light_mode = 1;
                } else if (pin_number == 0) {
                  stop_lights();
                }
                break;
            case 'B':
                set_led_brightness(pin_number);
                break;
            case 'P':
                if (mode == 'R') {
                  red = pin_number;
                } else if (mode == 'G') {
                  green = pin_number;
                } else if (mode == 'B') {
                  blue = pin_number;
                }
                defined_lights();
                break;
            default:
                break;
        }
    }
}

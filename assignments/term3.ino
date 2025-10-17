//Constant variables for each component pin
const int trigPin = 7;
const int echoPin = 8;
const int ledRedPin = 11;
const int ledGreenPin = 12;
const int RedRGBPin = 6;
const int BlueRGBPin = 5;
const int GreenRGBPin = 4;
const int buzzerPin = 13;

class LED {
 public:
  //Turns off specified LED if it reads the pin as active
   void TurnOFF(int ledPin) {
     if (digitalRead(ledPin)) {
     digitalWrite(ledPin, LOW);
     }
   }

   void TurnON(int ledPin) {
     digitalWrite(ledPin, HIGH);
   }

  //Pause length is specified, function turns LED on and off with interval
   void Blink(int ledPin, int pause) {
     digitalWrite(ledPin, HIGH);
     delay(pause);
     digitalWrite(ledPin, LOW);
     delay(pause);
   }
};

class Buzzer {
 public:
  //If program reads buzzer pin as active, turns off buzzer
   void TurnOFF() {
     if (digitalRead(buzzerPin)) {
     noTone(buzzerPin);
     }
   }

  //Pause amount and frequency specified, buzzer beeps according to these values
   void TurnON(int frequency, int pause) {
     tone(buzzerPin, frequency);
     delay(pause);
     noTone(buzzerPin);
     delay(pause);
   }
};


class Ultrasonic {
 public:
   //measureIncrease is the status;
   //Whether there is oncoming movement or not
   bool measureIncrease = false;
   //measureValue gets value of measure2 if distance decreases (object gets closer)
   int measureValue = 0;
   //measure1 and measure2 are placeholders for readings
   int measure1 = 0;
   int measure2 = 0;

  //Function converts the sensor's microsecond measure into centimetres
   long microsecondsToCentimetres(long microseconds) {
     return microseconds / 29 / 2;
   }

  //Function performs general sensor operation
   int Activate() {
     long duration;
     delay(30);
     //Short low pulse to obtain a clean high pulse
     digitalWrite(trigPin, LOW);
     delayMicroseconds(2);
     digitalWrite(trigPin, HIGH);
     delayMicroseconds(10);
     digitalWrite(trigPin, LOW);
     //Records duration of pulse
     duration = pulseIn(echoPin, HIGH);
     //Converts to centimetres, assigns as first measure
     measure1 = microsecondsToCentimetres(duration);
     delay(30);
     //Second trial
     digitalWrite(trigPin, LOW);
     delayMicroseconds(2);
     digitalWrite(trigPin, HIGH);
     delayMicroseconds(10);
     digitalWrite(trigPin, LOW);
     duration = pulseIn(echoPin, HIGH);
     //Assigns second centimetre value
     measure2 = microsecondsToCentimetres(duration);
     //Checks if the object is moving toward sensor (closer)
     if (measure1 > measure2) {
      //If closer, changes measureIncrease and assigns measureValue
       measureIncrease = true;
       measureValue = measure2;
     }
   }
};

class rgbLED {
 public:
   //Assign initial values of red, green and blue in LED. Starts as red.
   int rgbRed = 255;
   int rgbGreen = 0;
   int rgbBlue = 0;

  //To turn LED off, all values set to 0
   void TurnOFF() {
     setColour(0,0,0);
   }

  //Function to set the RGB colours, writing value to pin
  void setColour(int R, int G, int B) {
     analogWrite(RedRGBPin, R);
     analogWrite(GreenRGBPin, G);
     analogWrite(BlueRGBPin, B);
   }

  //To turn on, use setColour function and pass through the variables established at the top of the class
   void TurnON() {
     setColour(rgbRed, rgbGreen, rgbBlue);
   }

  //Function changes the values of red and green according to distance
   void PhaseColour(int distFromSensor) {
    //Counter to track iterations and compare to distance
     int counter = 0;
     while(!(counter >= distFromSensor)) {
      if (rgbGreen != 255) {
      //Phases from green, to yellow, to red when object moves closer
       rgbRed = rgbRed - 15;
       rgbGreen = rgbGreen + 15;
      }
      counter = counter + 24;
    }
   }
};

//Setting up all the pins as input or output, crucial for sensor
void setup() {
 Serial.begin(9600);
 pinMode(trigPin,OUTPUT);
 pinMode(echoPin,INPUT);
 pinMode(ledRedPin, OUTPUT);
 pinMode(ledGreenPin, OUTPUT);
 pinMode(RedRGBPin, OUTPUT);
 pinMode(GreenRGBPin, OUTPUT);
 pinMode(BlueRGBPin, OUTPUT);
 pinMode(buzzerPin, OUTPUT);
}

void loop() {
//Creating objects of each class
 LED redLED;
 LED greenLED;
 rgbLED rgb;
 Buzzer buzz;
 Ultrasonic sensor;

//Begin by activating sensor
 sensor.Activate();
 bool state = sensor.measureIncrease;
 //Loops until sensor detects oncoming movement
 while (state = false) {
   sensor.Activate();
   bool state = sensor.measureIncrease;
 }

 int distance = sensor.measureValue;

//Checks what range distance falls into and calls appropriate functions
//Range beyond 3.5 metres
 if (distance > 350) {
   buzz.TurnOFF();
   redLED.TurnOFF(ledRedPin);
   rgb.TurnOFF();
   greenLED.TurnON(ledGreenPin);
//Range within 3.5 metres and 0.5 metres
 } else if ((distance<=350) && (distance>=50)) {
   buzz.TurnOFF();
   buzz.TurnON(200, 300);
   rgb.PhaseColour(distance);
   greenLED.TurnOFF(ledGreenPin);
   redLED.TurnOFF(ledRedPin);
   rgb.TurnON();
//Range within 0.5 metres and 0 metres (the edge)
 } else if ((distance > 0) && (distance < 50)) {
   buzz.TurnOFF();
   buzz.TurnON(500, 200);
   greenLED.TurnOFF(ledGreenPin);
   rgb.TurnOFF();
   redLED.Blink(ledRedPin, 200);
//Zero or beyond; turns off
 } else {
   redLED.TurnOFF(ledRedPin);
   greenLED.TurnOFF(ledGreenPin);
   rgb.TurnOFF();
   buzz.TurnOFF();
 }
}

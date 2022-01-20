void Decoder();
void LED1Function();

// Serial Stuff
const byte NumChars = 128;
char ReceivedChars[NumChars];
bool NewData = false;
bool NewDataNotDealtWith = false;

// Millis 
unsigned long CurrentMillis;

// LED Flags and Millis
bool LED1Flag = false;
bool LED2Flag = false;

byte LEDMillisInterval = 50;
unsigned long PreviousLED1Millis;
unsigned long PreviousLED2Millis;


const byte LED1 = 2;
const byte LED2 = 4;




/*
 * TODO: Millis
 * Setup of Flags for LEDs
 * Decoder Function
 * Handshake Readback
 * 
 * 
 */

/* Variable Optimisation Guide:
 *  
 *  bool
 *  
 *  byte
 *  byte is unsigned from 0 to 255
 *  
 *  int
 *  
 *  
 *  unsigned int
 *  
 *  
 *  
 *  
 * Flags -> Use bool, either true or false
 * 
 * 
 * 
 * Use static for variables that will remain inside the loop
 * Stuff like: 
 *  Count etc
 * 
 * 
 */





void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200); // Use highest officially supported baudrate on Arduino Uno
  
  Serial.print("<Arduino Is Ready>"); // Required for Python
  /*
   *  Standard Handshake Setup
   *  Serial Communication resets the Arduino Uno, starting the setup sequence
   *  
   */
   /*
    * PinMode Setup
    * Right now Idea is 5 LEDs
    * 2 RGB LEDs, might not have enough IO
    * 5 + 6?
    * Ideally reserve another pin for DC motor or servo motor
    * Need to assign RGB LED Pinout to PWM
    * 
    * Uno PWM Pins are 3, 5, 6, 9, 10 and 11
    * 
    * 3,5,6 for RGB LED 1
    * 9, 10 and 11 for RGB LED2
    * 
    * 0 RX
    * 1 TX
    * 2 LED 1
    * 3 RGB LED 1 R CHANNEL
    * 4 LED 2
    * 5 RGB LED 1 G CHANNEL
    * 6 RGB LED 1 B CHANNEL
    * 7 LED 3
    * 8 LED 4
    * 9 RGB LED 2 R CHANNEL
    * 10 RGB LED 2 G CHANNEL
    * 11 RGB LED 2 B CHANNEL
    * 12 LED 5
    * 13 APPLIANCE 1
    * 
    * Seems ok for the assignment, maybe cut 1 LED and put in another appliance?
    * Ideally would use LED strips, concerned about time/implementation of that as well
    * Doesnt seem like there is enough time for that
    * 
    * 
    */
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, LOW);

    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);
    
    



  
}

void loop() {
  // put your main code here, to run repeatedly:
  /*
   * Run Decoder followed by functions
   * Is a polling method 
   * 
   */
   CurrentMillis = millis();
   ReceiveCharsWithStartAndEndMarkers();
   Decoder();





   
}

void ReceiveCharsWithStartAndEndMarkers(){
  static bool ReceiveInProgress = false;
  static byte count = 0;
  char StartMarker = '<';
  char EndMarker = '>';
  char ReceivedCharacter;

  while (Serial.available() > 0 && NewData == false) {

    ReceivedCharacter = Serial.read();

    if (ReceiveInProgress == true) {

      if (ReceivedCharacter != EndMarker) {

        ReceivedChars[count] = ReceivedCharacter;
        count++;

        if (count >= NumChars) {

          count = NumChars - 1;

        }

      }
      else {
        ReceivedChars[count] = '\0';
        ReceiveInProgress = false;
        count = 0;
        NewData = true;
      }
    }
    else if (ReceivedCharacter == StartMarker) {

      ReceiveInProgress = true;

    }

  }

}

void Decoder(){
  if(NewData == true){
    
    String ReceivedString = ReceivedChars;
    
    if(ReceivedString == "Comm Check"){

      Serial.print("<Readback>");
      
    }
    else if(ReceivedString == "Testing"){

      digitalWrite(LED_BUILTIN, HIGH);

    }
    /*
     * To make a unique call for on/off? Or just a call to toggle the light 
     * Might have to introduce some delay into the python script, scared it'll spam the crap out of the serial port
     * Have to do some testing on this
     * Test without any delays and see how bad it is 
     */
     
    else if(ReceivedString == "LED1HIGH"){

      LED1Flag = true;
    
    }

    else if(ReceivedString == "LED1LOW"){

      
    
    }

    /*
    else if(ReceivedString == ""){

      
    
    }
    */



    
    NewData = false;
    
  }
}

void LED1Function(){

  static bool LED1Status = LOW;

  if(LED1Flag & PreviousLED1Millis - CurrentMillis >= LEDMillisInterval){

    if(LED1Status == LOW){
      digitalWrite(LED2, HIGH);
      LED1Status = HIGH;
    }
    else{
      digitalWrite(LED1, LOW);
      LED1Status = LOW;
    }
    LED1Flag = false;
  }
  
  
}

// Idea is to just copy paste the LED Functions

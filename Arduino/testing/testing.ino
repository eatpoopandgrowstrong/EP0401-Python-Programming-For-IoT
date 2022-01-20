void Decoder();

const byte NumChars = 128;

char ReceivedChars[NumChars];
boolean NewData = false;
boolean NewDataNotDealtWith = false;

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
 *  boolean
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
 * Flags -> Use boolean, either true or false
 * 
 * 
 * 
 * Use static for variables that will remain inside the loop
 * Stuff like: 
 *  Count etc
 * 
 *  
 * 
 * 
 * 
 * 
 * 
 */


unsigned long CurrentMillis;

//unsigned long 
boolean LEDFlag = false;





const byte LED1 = 2;
const byte LED2 = 4;

/*
const byte
const byte
const byte
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
  


    
  
}

void loop() {
  // put your main code here, to run repeatedly:
  /*
   * Run Decoder followed by functions
   * 
   * 
   */
   CurrentMillis = millis();
   ReceiveCharsWithStartAndEndMarkers();
   Decoder();





   
}

void ReceiveCharsWithStartAndEndMarkers(){
  static boolean ReceiveInProgress = false;
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
    NewData = false;
    
  } 
}

void LEDTestFunction(){


  
}

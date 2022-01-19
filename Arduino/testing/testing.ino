/*
 * TODO: Millis
 * Setup of Flags for LEDs
 * Decoder Function
 * Handshake Readback
 * 
 * 
 */

/* Variable Optimisation Guide:
 * Flags -> Use boolean, either true or false
 * 
 * 
 * 
 * 
 * 
 * 
 */


unsigned long CurrentMillis;

unsigned long 
boolean LEDFlag = false;








void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200); // Use highest officially supported baudrate on Arduino Uno

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
    * 
    */
    //pinMode();



    
  
}

void loop() {
  // put your main code here, to run repeatedly:
  /*
   * Run Decoder followed by functions
   * 
   * 
   */
   CurrentMillis = millis()





   
}

void DecoderFunction(){

  
}

void LEDTestFunction(){


  
}

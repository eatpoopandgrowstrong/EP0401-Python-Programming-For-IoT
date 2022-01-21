

int SwitchValue;
char SwitchValues;

void setup(){

  Serial.begin(115200);
  
}


void loop(){

  // Idea is to optimise the decoder function, instead of using a bunch of if else, use a switch and cases
  // Problem is that switch case only accepts char or int


  Serial.read();

  Decoder();




  
  
}


void Decoder(){

  switch (SwitchValue){
    case 1:
    // Do stuff here
    break;
  
    default:
  
    break;
  }
  

  
  
}

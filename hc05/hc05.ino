    #include <SoftwareSerial.h>

    int buttonState = 0;
    SoftwareSerial EEBlue(10, 11); // RX | TX
    //const int buttonPin = 0;
    void setup()
    {
      Serial.begin(9600);
      EEBlue.begin(9600);  //Default Baud for comm, it may be different for your Module. 
      
    }
     
    void loop(){

      //buttonState = Serial.write(buttonPin);
     
      // Feed any data from bluetooth to Terminal.
      if (EEBlue.available())
        Serial.write(EEBlue.read());
     
      // Feed all data from termial to bluetooth
      if (Serial.available())
      EEBlue.write(Serial.read());

      //Serial.println("I Love You, ");
      delay(1000);  
      Serial.println("I Love you baby,");
      delay(1000);  
      Serial.println("Sin dee you are my love");
      delay(1000);  
      Serial.println("Sayang sayang <3");
      delay(1000);  


      if (buttonState == HIGH){
        Serial.println("I Love My Wife");
        } else {
          delay(1000);
          }
    }

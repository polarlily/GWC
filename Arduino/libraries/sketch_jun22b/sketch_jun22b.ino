void setup() {
  Serial.begin(9600);
}

char user_number = 0;

void loop() {
  if (Serial.available() > 0) {    // is a character available?
    user_number = Serial.read();       // get the character
  
    // check if a number was received
    if ((user_number >= '0') && (user_number <= '9')) {
      Serial.print("Number received: ");
      Serial.println(user_number);
    }
    else {
      Serial.println("Not a number.");
    }
  } // end: if (Serial.available() > 0)
}

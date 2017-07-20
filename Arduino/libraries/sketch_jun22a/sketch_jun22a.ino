
/*-----( Import needed libraries )-----*/
/*-----( Declare Constants and Pin Numbers )-----*/
#define led 13  // built-in LED
/*-----( Declare objects )-----*/
/*-----( Declare Variables )-----*/
int ByteReceived;

void setup()   /****** SETUP: RUNS ONCE ******/
{
  Serial.begin(9600);
    while (! Serial);
    Serial.println("Hello!");  
    Serial.println("What is your favorite color?");  
}
//--(end setup )---

void loop()   /****** LOOP: RUNS CONSTANTLY ******/
{
  if (Serial.available())
  {
    String color = String(Serial.readString());
    Serial.print("That's Awesome! I like " + color + ", but I prefer Magenta.");
      
  }
  Conversation :
  if (Serial.available())
  {
    String season = String(Serial.readString());
    Serial.print("What's Your favorite season?");
  }
 }

  


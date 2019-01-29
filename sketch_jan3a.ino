int ledPin=13;
int delayPeriod=500;
void setup() {
  // put your setup code here, to run once:
pinMode(ledPin,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
for(int i=0;i<20;i++)
{
  digitalWrite(ledPin,HIGH);
  delay(delayPeriod);
  digitalWrite(ledPin,LOW);
  delay(delayPeriod);
}
delay(delayPeriod*6);
}

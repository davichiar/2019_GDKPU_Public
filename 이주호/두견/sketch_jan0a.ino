int ledPin=13;
int delayPeriod=500;

void setup() {
  // put your setup code here, to run once:
pinMode(ledPin,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(ledPin,HIGH);
delay(delayPeriod);
digitalWrite(ledPin,HIGH);
delay(delayPeriod);
}

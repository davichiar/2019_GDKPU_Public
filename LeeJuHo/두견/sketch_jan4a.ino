int ledPin=13;
int delayPeriod=500;

void setup() {
  // put your setup code here, to run once:
pinMode(ledPin,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  int count = 0;
while(count<20){
  digitalWrite(ledPin,HIGH);
  delay(delayPeriod);
  digitalWrite(ledPin,LOW);
  delay(delayPeriod);
  count++;
}
delay(delayPeriod);
}

void setup()
{
  pinMode(2, INPUT);
  pinMode(12, OUTPUT);
}

void loop()
{
  if (digitalRead(2) == HIGH) {
    digitalWrite(12, HIGH);
  } else {
    digitalWrite(12, LOW);
  }
  delay(10); // Delay a little bit to improve simulation performance
}
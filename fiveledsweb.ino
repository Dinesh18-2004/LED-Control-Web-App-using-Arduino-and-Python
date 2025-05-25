const int ledPins[] = {13, 11, 9}; // Pins for the LEDs
const int numLeds = 3;

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < numLeds; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    if (command == "ALL_ON") {
      for (int i = 0; i < numLeds; i++) {
        digitalWrite(ledPins[i], HIGH);
      }
    } else if (command == "ALL_OFF") {
      for (int i = 0; i < numLeds; i++) {
        digitalWrite(ledPins[i], LOW);
      }
    } else {
      for (int i = 0; i < numLeds; i++) {
        if (command == "LED" + String(i + 1) + "_ON") {
          digitalWrite(ledPins[i], HIGH);
        } else if (command == "LED" + String(i + 1) + "_OFF") {
          digitalWrite(ledPins[i], LOW);
        }
      }
    }
  }
}

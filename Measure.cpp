#define TRIG_PIN 9
#define ECHO_PIN 10

void setup() {
  Serial.begin(9600);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  long duration;
  float distanceCm, distanceIn;

  // Send a 10us pulse to trigger pin
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Read the echo pin
  duration = pulseIn(ECHO_PIN, HIGH);

  // Calculate the distance in cm and inches
  distanceCm = (duration * 0.034) / 2;  // Speed of sound in air: 343m/s
  distanceIn = distanceCm / 2.54;

  // Print the results
  Serial.print("Distance: ");
  Serial.print(distanceCm);
  Serial.print(" cm, ");
  Serial.print(distanceIn);
  Serial.println(" inches");

  delay(500);
}

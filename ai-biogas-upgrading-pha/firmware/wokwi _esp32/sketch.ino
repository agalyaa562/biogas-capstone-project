const int SENSOR_PIN = 34;
const int STAGE_PIN  = 2;
const float CO2_ON   = 40.0;   // % threshold
const float CO2_OFF  = 35.0;   // hysteresis
bool stageOn = false;

void setup() {
  Serial.begin(115200);
  pinMode(STAGE_PIN, OUTPUT);
}

void loop() {
  int raw = analogRead(SENSOR_PIN);
  float co2 = (raw / 4095.0) * 60.0;   // simulated 0-60% CO2

  if (co2 > CO2_ON)  stageOn = true;
  if (co2 < CO2_OFF) stageOn = false;
  digitalWrite(STAGE_PIN, stageOn);

  Serial.printf("CO2: %.1f %% | Stage: %s\n", co2, stageOn ? "ON" : "OFF");
  delay(1000);
}
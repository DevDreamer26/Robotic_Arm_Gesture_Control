#include <Servo.h>

Servo servo1, servo2, servo3, servo4, servo5;
const int servoPins[5] = {3, 5, 6, 9, 10};  // Servo pins

void setup() {
    Serial.begin(9600);  // Start Serial Communication

    // Attach Servos
    servo1.attach(servoPins[0]);
    servo2.attach(servoPins[1]);
    servo3.attach(servoPins[2]);
    servo4.attach(servoPins[3]);
    servo5.attach(servoPins[4]);

    Serial.println("Ready to receive data...");
}

void loop() {
    if (Serial.available() > 0) {
        String data = Serial.readStringUntil('\n');  // Read incoming data
        int angles[5];  // Array to store received angles

        // Parse angles from received string (Format: "30,45,90,10,60")
        int index = 0;
        char *token = strtok((char *)data.c_str(), ",");
        while (token != NULL && index < 5) {
            angles[index] = atoi(token);
            token = strtok(NULL, ",");
            index++;
        }

        // Move servos to received angles
        servo1.write(angles[0]);
        servo2.write(angles[1]);
        servo3.write(angles[2]);
        servo4.write(angles[3]);
        servo5.write(angles[4]);

        Serial.println("Servo positions updated!");
    }
}

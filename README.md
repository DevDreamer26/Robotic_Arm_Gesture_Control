# 📌 Robotic Arm Hand Gesture Control

🚀 An AI-powered robotic arm that mimics hand gestures in real-time using OpenCV, MediaPipe, and Arduino.

---

## 📜 Project Description

This project implements a gesture-controlled robotic arm using computer vision and servo motors. The system captures real-time hand movements using a webcam, processes finger positions with MediaPipe, and controls 5 servo motors via Arduino, ensuring each finger movement is accurately replicated by the robotic arm.

---

## 🛠 Hardware Requirements

* Arduino Uno / Mega / Nano
* 5 Servo Motors (SG90 / MG995)
* External Power Supply (5V, 2A recommended)
* USB Cable (For Arduino-PC communication)
* Webcam (Laptop Camera or USB Webcam)
* Jump Wires & Breadboard

---

## 💻 Software Requirements

* Python 3.x
* OpenCV (cv2)
* MediaPipe
* PySerial (For Arduino communication)
* Arduino IDE (To upload code to Arduino)

---

## 📁 Folder Structure

```bash
Robotic_Arm_Gesture_Control/
│── hardware/
│   ├── circuit_diagram.png
│   ├── robotic_arm.ino  # Arduino Code
│
│── software/
│   ├── main.py          # Hand tracking & Arduino communication
│   ├── requirements.txt # Dependencies
│
│── README.md




<p align="center">
  <img src="/hardware/images/project_status_1" alt="Project Image 1" width="400" height="300">
  <img src="/hardware/images/project_status_2" alt="Project Image 2" width="400" height="300">
</p>




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
```
## 🔧 Installation & Setup

1️⃣ **Install Dependencies**

Run the following command to install all required Python libraries:

```bash
pip install opencv-python mediapipe pyserial numpy
```

2️⃣ Upload Arduino Code

Open robotic_arm.ino in the Arduino IDE.
Select the correct Board and Port.
Upload the code to Arduino.

3️⃣ Run the Python Script

Execute the following command in the terminal:
```bash
python main.py
```
After completing these steps, the robotic arm should begin mirroring your hand gestures. Ensure all hardware connections are secure and the webcam is properly positioned.

---

## 🖥 Working Principle

* **Hand Detection** → The webcam captures real-time video.
* **Finger Tracking** → MediaPipe extracts finger landmarks.
* **Angle Calculation** → The bending angle of each finger is computed.
* **Servo Control** → The corresponding servo motors are rotated to match hand gestures.
* **Live Mimicry** → The robotic arm mimics your finger movements in real-time!

---

## 🤖 Demo Video & Output

🎥 Working on it and will be available soon, stay tuned ❤️‍🔥

---

## 🎯 Future Improvements

* 🛡 **Add Wireless Communication:** (ESP8266 / Bluetooth module) for remote control and flexibility.
* 🔋 **Battery-Powered Version:** for standalone use, enabling portability.
* 📡 **Cloud Connectivity:** for advanced remote control and data logging capabilities.
* ✨ **Improved Accuracy and Smoothness:** through advanced calibration and filtering algorithms.
* 🤖 **Grip and Object Manipulation:** adding a gripper to the robotic arm for practical applications.
* 🎨 **Customizable Design:** allowing users to modify the arm's appearance and functionality.
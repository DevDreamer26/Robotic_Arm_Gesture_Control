import cv2
import mediapipe as mp
import serial
import time
import numpy as np

# Initialize Serial Communication
arduino = serial.Serial('COM9', 9600)
time.sleep(2)  # Give time for Arduino to reset

# Initialize MediaPipe Hand Tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Finger Landmarks
FINGER_TIPS = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky
FINGER_BASES = [6, 10, 14, 18]  # Lower joints

THUMB_TIP = 4
THUMB_BASE = 2

# Function to Calculate Finger Bend Angle
def calculate_angle(finger_tip, finger_base):
    dx = finger_tip.x - finger_base.x  # Correct way to access x-coordinates
    dy = finger_tip.y - finger_base.y  # Correct way to access y-coordinates
    angle = np.arctan2(dy, dx) * (180 / np.pi)  # Convert to degrees
    return int(np.interp(angle, [-90, 90], [0, 180]))  # Normalize to 0-180°


# Open Camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert Frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract Finger Angles
            servo_angles = []

            # Thumb Angle
            thumb_angle = calculate_angle(hand_landmarks.landmark[THUMB_TIP], hand_landmarks.landmark[THUMB_BASE])
            servo_angles.append(thumb_angle)

            # Other Four Fingers
            for i in range(4):
                angle = calculate_angle(hand_landmarks.landmark[FINGER_TIPS[i]], hand_landmarks.landmark[FINGER_BASES[i]])
                servo_angles.append(angle)

            # Send Data Only If Angles Have Changed
            angle_str = ",".join(map(str, servo_angles))  # Convert list to comma-separated string
            arduino.write((angle_str + "\n").encode())  # Send to Arduino
            print("Sent:", angle_str)

    # Show Video Feed
    cv2.imshow("Hand Gesture Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
arduino.close()

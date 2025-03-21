import cv2
import mediapipe as mp
import serial
import time

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7)
arduino = serial.Serial('COM3', 9600)  

def get_finger_states(hand_landmarks):
    tip_ids = [8, 12, 16, 20]
    return [1 if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y else 0 for tip in tip_ids]

def send_to_arduino(finger_states):
    command = ','.join(map(str, finger_states)) + '\n'
    arduino.write(command.encode())
    time.sleep(0.1)

def run():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                finger_states = get_finger_states(hand_landmarks)
                send_to_arduino(finger_states)

        cv2.imshow("Gesture Controlled Robotic Arm", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()

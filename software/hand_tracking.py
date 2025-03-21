import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7)

def get_finger_states(hand_landmarks):
    tip_ids = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky finger tips
    states = []

    for tip in tip_ids:
        tip_y = hand_landmarks.landmark[tip].y
        base_y = hand_landmarks.landmark[tip - 2].y
        states.append(1 if tip_y < base_y else 0)  # 1 = Open, 0 = Closed

    return states

def detect_hand():
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
                print(f"Finger States: {finger_states}")

        cv2.imshow("Hand Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_hand()

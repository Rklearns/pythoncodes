import cv2
import mediapipe as mp
import pyautogui
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)

cap = cv2.VideoCapture(0)

def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def display_text(frame, text, position, color=(0, 255, 0)):
    cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

            h, w, _ = frame.shape
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)
            middle_x, middle_y = int(middle_tip.x * w), int(middle_tip.y * h)

            distance_thumb_index = calculate_distance((thumb_x, thumb_y), (index_x, index_y))
            distance_thumb_middle = calculate_distance((thumb_x, thumb_y), (middle_x, middle_y))

            if distance_thumb_index < 50:
                pyautogui.press("volumedown")
                display_text(frame, "Volume Down", (30, 30))
                print("Volume down")
            elif distance_thumb_index > 150:
                pyautogui.press("volumeup")
                display_text(frame, "Volume Up", (30, 30))
                print("Volume up")
            else:
                volume_level = int(distance_thumb_index / 10)
                volume_level = min(max(volume_level, 0), 100)
                pyautogui.press(f"volumeup {volume_level}")
                display_text(frame, f"Volume: {volume_level}%", (30, 30))
                print(f"Volume set to {volume_level}%")

            if distance_thumb_middle < 40:
                pyautogui.click()
                display_text(frame, "Click", (30, 60), color=(0, 0, 255))
                print("Mouse Clicked")

    cv2.imshow("Hand Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

import cv2
import mediapipe as mp
import pyautogui

# Setup MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Webcam setup
cap = cv2.VideoCapture(0)
prev_y = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Mirror view
    h, w, _ = img.shape

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get index finger tip coordinates (id = 8)
            index_tip = hand_landmarks.landmark[8]
            x = int(index_tip.x * w)
            y = int(index_tip.y * h)

            cv2.circle(img, (x, y), 10, (0, 255, 0), cv2.FILLED)
            cv2.putText(img, f"Index: ({x}, {y})", (10, 40), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

            if prev_y != 0:
                if y < prev_y - 20:
                    pyautogui.scroll(50)  # Scroll up
                elif y > prev_y + 20:
                    pyautogui.scroll(-50)  # Scroll down

            prev_y = y

    cv2.imshow("Scroll Using Gestures", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

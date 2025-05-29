import cv2
import mediapipe as mp
import time
import os

# Create folder to save photos
if not os.path.exists("Captured_Images"):
    os.makedirs("Captured_Images")

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Access webcam
cap = cv2.VideoCapture(0)
photo_count = 0
cooldown = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, _ = img.shape
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Get coordinates of fingers
        landmarks = hand_landmarks.landmark

        # Tips: Thumb = 4, Index = 8, Middle = 12
        thumb_up = landmarks[4].y < landmarks[3].y
        index_up = landmarks[8].y < landmarks[6].y
        middle_up = landmarks[12].y < landmarks[10].y

        # Condition to take photo
        if (index_up and middle_up and not thumb_up) or thumb_up:
            if cooldown == 0:
                photo_count += 1
                filename = f"Captured_Images/photo_{photo_count}_{int(time.time())}.png"
                cv2.imwrite(filename, img)
                print(f"[✅] Photo saved as: {filename}")
                cooldown = 30  # Wait 30 frames to prevent rapid capture
                cv2.putText(img, "Photo Captured!", (50, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    if cooldown > 0:
        cooldown -= 1

    cv2.imshow("Gesture-Controlled Photo App", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

import cv2
import numpy as np
import mediapipe as mp
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc

# MediaPipe hand detection setup
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

# Access webcam
cap = cv2.VideoCapture(0)

# Pycaw setup for volume control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume_ctrl = cast(interface, POINTER(IAudioEndpointVolume))

vol_min, vol_max = volume_ctrl.GetVolumeRange()[:2]

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Flip for mirror effect
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    lmList = []
    if results.multi_hand_landmarks:
        handLms = results.multi_hand_landmarks[0]
        for id, lm in enumerate(handLms.landmark):
            h, w, _ = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmList.append((id, cx, cy))

        mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        if lmList:
            # Thumb tip = id 4, Index finger tip = id 8
            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[8][1], lmList[8][2]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            # Draw line & circles
            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.circle(img, (cx, cy), 8, (255, 255, 0), cv2.FILLED)

            # Calculate distance
            length = math.hypot(x2 - x1, y2 - y1)

            # Convert distance to volume range
            vol = np.interp(length, [30, 200], [vol_min, vol_max])
            volume_ctrl.SetMasterVolumeLevel(vol, None)

            # Convert to brightness range (0-100)
            brightness = int(np.interp(length, [30, 200], [0, 100]))
            sbc.set_brightness(brightness)

            # Display volume & brightness
            cv2.putText(img, f'Volume: {int(np.interp(length, [30, 200], [0, 100]))}%', (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.putText(img, f'Brightness: {brightness}%', (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show image
    cv2.imshow("Volume & Brightness Control", img)

    # Break loop with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

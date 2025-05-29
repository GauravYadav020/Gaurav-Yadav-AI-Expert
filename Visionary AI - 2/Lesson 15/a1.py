import cv2
import mediapipe as mp

# Initialize MediaPipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the image and detect hands
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw landmarks and connections
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get coordinates of the tip of the index finger (landmark 8)
            x = int(hand_landmarks.landmark[8].x * img.shape[1])
            y = int(hand_landmarks.landmark[8].y * img.shape[0])

            # Draw a circle at index fingertip
            cv2.circle(img, (x, y), 10, (255, 0, 0), cv2.FILLED)

            # Display coordinates
            cv2.putText(img, f'Index Tip: ({x},{y})', (10, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    # Show the image
    cv2.imshow("Gesture Control Basics", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

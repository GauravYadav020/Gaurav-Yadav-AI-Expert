import cv2

# Initialize webcam
cap = cv2.VideoCapture(0)

# Set default mode
mode = 'original'

print("Press keys to switch modes:")
print("r - Red Filter")
print("g - Green Filter")
print("b - Blue Filter")
print("e - Edge Detection")
print("o - Original")
print("q - Quit")

while True:
    # Read frame
    ret, frame = cap.read()
    
    # Apply filter based on mode
    if mode == 'red':
        filtered = frame.copy()
        filtered[:, :, 0] = 0  # Remove blue
        filtered[:, :, 1] = 0  # Remove green

    elif mode == 'green':
        filtered = frame.copy()
        filtered[:, :, 0] = 0  # Remove blue
        filtered[:, :, 2] = 0  # Remove red

    elif mode == 'blue':
        filtered = frame.copy()
        filtered[:, :, 1] = 0  # Remove green
        filtered[:, :, 2] = 0  # Remove red

    elif mode == 'edge':
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        filtered = cv2.Canny(gray, 100, 200)

    else:
        filtered = frame

    # Display the result
    cv2.putText(frame, f'Mode: {mode}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                1, (0, 255, 255), 2)
    
    # Show appropriate window based on mode
    if mode == 'edge':
        cv2.imshow('Filtered Output', filtered)
    else:
        cv2.imshow('Filtered Output', filtered)

    # Wait for key press
    key = cv2.waitKey(1) & 0xFF

    # Switch modes based on key
    if key == ord('r'):
        mode = 'red'
    elif key == ord('g'):
        mode = 'green'
    elif key == ord('b'):
        mode = 'blue'
    elif key == ord('e'):
        mode = 'edge'
    elif key == ord('o'):
        mode = 'original'
    elif key == ord('q'):
        break

# Release and close
cap.release()
cv2.destroyAllWindows()

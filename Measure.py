import cv2
import numpy as np

# Constants (calibration values)
KNOWN_WIDTH = 14.0  # Width of the object in cm (or inches)
FOCAL_LENGTH = 700  # Focal length of your camera in pixels (calibrate this value)

def calculate_distance(known_width, focal_length, perceived_width):
    """Calculate the distance of the object from the camera."""
    return (known_width * focal_length) / perceived_width

# Initialize camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera not accessible.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Frame capture failed.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Ignore small objects
            x, y, w, h = cv2.boundingRect(contour)

            # Calculate distance
            distance = calculate_distance(KNOWN_WIDTH, FOCAL_LENGTH, w)

            # Display on frame
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"Distance: {distance:.2f} cm", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Distance Measurement", frame)

    # Break loop with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

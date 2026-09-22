import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera could not be opened.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not read camera.")
        break

    # Object detection and tracking
    results = model.track(frame, persist=True)

    # Draw boxes, labels and tracking IDs
    output = results[0].plot()

    # Show camera
    cv2.imshow("CodeAlpha - Object Detection and Tracking", output)

    # Press Q to stop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
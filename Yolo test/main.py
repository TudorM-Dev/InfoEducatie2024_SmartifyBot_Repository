# pip install ultralytics

import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
print(model.names)
webcamera = cv2.VideoCapture(1, cv2.CAP_DSHOW)

while True:
    success, frame = webcamera.read()
    
    results = model.predict(frame, classes=0, conf=0.5)
    cv2.putText(frame, f"Total: {len(results[0].boxes)}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("Live Camera", results[0].plot())

    if cv2.waitKey(1) == ord('q'):
        break

webcamera.release()
cv2.destroyAllWindows()

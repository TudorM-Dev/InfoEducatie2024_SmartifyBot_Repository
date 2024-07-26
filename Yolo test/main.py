# pip install ultralytics

import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
# print(model.names)
webcamera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while webcamera.isOpened():
    success, frame = webcamera.read()
    
    results = model(frame, conf=0.7)
    # cv2.putText(frame, f"Total: {len(results[0].boxes)}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    # cv2.imshow("Predicted Camera", results[0].plot())
    # # cv2.imshow("Live Camera", frame)
        # Process results list
    for result in results:
        # boxes = result.boxes  # Boxes object for bounding box outputs
        # masks = result.masks  # Masks object for segmentation masks outputs
        # keypoints = result.keypoints  # Keypoints object for pose outputs
        # probs = result.probs  # Probs object for classification outputs
        obb = result.obb  # Oriented boxes object for OBB outputs
        result.show()  # display to screen
        cv2.imshow("Predicted Camera", results[0].plot())

    


    if cv2.waitKey(1) == ord('q'):
        break

webcamera.release()
cv2.destroyAllWindows()

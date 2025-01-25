import cv2
from ultralytics import YOLO

def process_video(video_path, video_queue):
    """Process video frames for hazard detection using YOLO model."""
    model = YOLO('yolov8n.pt')
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        detections = results.pandas().xyxy[0]

        hazards = [
            {"object": row['name'], "hazard": "Potential Risk"}
            for _, row in detections.iterrows() if row['name'] == "person"
        ]

        video_queue.append(hazards)

        annotated_frame = results.render()[0]
        cv2.imshow("Hazard Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

import cv2
import numpy as np

class ObjectDetection:
    def __init__(self, model_path, config_path, class_names_path):
        self.net = cv2.dnn.readNet(model_path, config_path)
        self.classes = self.load_classes(class_names_path)

    def load_classes(self, class_names_path):
        with open(class_names_path, "r") as f:
            return f.read().strip().split("\n")

    def detect_players(self, frame):
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
        self.net.setInput(blob)
        layer_names = self.net.getUnconnectedOutLayersNames()
        outs = self.net.forward(layer_names)

        detected_players = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5 and self.classes[class_id] == "person":
                    x, y, w, h = map(int, detection[0:4] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]]))
                    detected_players.append((x, y, x + w, y + h))
        
        return detected_players

if __name__ == "__main__":
    # Example usage:
    model_path = "yolov3.weights"
    config_path = "yolov3.cfg"
    class_names_path = "coco.names"

    video_file = "basketball_game.mp4"

    detection_module = ObjectDetection(model_path, config_path, class_names_path)

    cap = cv2.VideoCapture(video_file)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detected_players = detection_module.detect_players(frame)

        for player in detected_players:
            x1, y1, x2, y2 = player
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv2.imshow("Object Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

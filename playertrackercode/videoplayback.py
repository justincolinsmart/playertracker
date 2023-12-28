import cv2

class VideoPlayer:
    def __init__(self, video_file):
        self.cap = cv2.VideoCapture(video_file)

    def initialize(self):
        if not self.cap.isOpened():
            print("Error: Could not open video file.")
            exit(1)

    def get_next_frame(self):
        ret, frame = self.cap.read()
        if ret:
            return frame
        else:
            return None

    def display_frame(self, frame):
        cv2.imshow("Basketball Game", frame)

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Example usage:
    video_file = "basketball_game.mp4"

    # Initialize the VideoPlayer before creating an instance
    player = VideoPlayer(video_file)
    player.initialize()

    while True:
        frame = player.get_next_frame()
        if frame is None:
            break

        player.display_frame(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    player.release()

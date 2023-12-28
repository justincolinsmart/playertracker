# main.py
import cv2
import videoplayback 
import objectdetection  
import playerrecognition 
import playertracking  
import userinteraction  
import datastorage  

# Creating instances of each module
video_player = videoplayback.VideoPlayer("path/to/your/video/file")  # Update the path
object_detector = objectdetection.ObjectDetection("model/path", "config/path", "classes/path")  # Update paths
player_recognizer = playerrecognition.PlayerRecognition()
player_tracker = playertracking.PlayerTracking()
ui_app = userinteraction.PlayerTrackingApp()  # This might need a root window if it's a tkinter app
data_store = datastorage.PlayerDatabase("path/to/your/database.db")  # Update the database path

# Initialize (if needed)
# Assuming some classes might need explicit initialization
video_player.initialize()
object_detector.initialize()  # Add this method in ObjectDetection class if required
player_tracker.initialize_sort()  # If the tracker needs initialization
ui_app.initialize()  # Add this method in PlayerTrackingApp class if required
data_store.initialize()  # Add this method in PlayerDatabase class if required

# Main loop
while True:
    frame = video_player.get_next_frame()
    if frame is None:
        break

    detected_players = object_detector.detect_players(frame)
    recognized_players = player_recognizer.recognize_players(detected_players)
    tracked_players = player_tracker.update(frame, recognized_players)
    ui_app.handle_input()  # Make sure this method exists and is appropriate for your UI logic
    data_store.save_player_data(tracked_players)  # Adjust the method name and parameters as needed
    video_player.display_frame(frame)

# Cleanup
video_player.release()
cv2.destroyAllWindows()

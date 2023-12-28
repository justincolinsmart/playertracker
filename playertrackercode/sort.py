import numpy as np

class Sort:
    def __init__(self):
        self.next_id = 0
        self.tracks = []

    def update(self, detections):
        # Implement the SORT update logic here
        # This is a simplified version, and the actual SORT implementation can be more complex
        
        # Create an empty list for updated tracks
        updated_tracks = []
        
        # Update existing tracks
        for track in self.tracks:
            # Perform track update logic here (e.g., predict track position, match with detections)
            # For simplicity, we'll assume the track remains unchanged
            updated_tracks.append(track)
        
        # Create new tracks for unassigned detections
        unassigned_detections = list(range(len(detections)))
        for track in updated_tracks:
            if track['assigned_detection'] is not None:
                unassigned_detections.remove(track['assigned_detection'])
        
        for detection_idx in unassigned_detections:
            # Create a new track for unassigned detection
            new_track = {
                'id': self.next_id,
                'bbox': detections[detection_idx],
                'assigned_detection': detection_idx,
            }
            updated_tracks.append(new_track)
            self.next_id += 1
        
        # Update the tracks list with the updated tracks
        self.tracks = updated_tracks
        
        # Return the updated list of tracks
        return self.tracks

if __name__ == "__main__":
    # Example usage:
    tracker = Sort()

    # Example detections (represented as bounding boxes [x1, y1, x2, y2])
    detections = [
        [100, 100, 200, 200],
        [300, 300, 400, 400],
        [150, 150, 250, 250]
    ]

    updated_tracks = tracker.update(detections)

    for track in updated_tracks:
        print(f"Track ID: {track['id']}, Bounding Box: {track['bbox']}")

import cv2
import numpy as np
from sort import Sort  # Make sure you have the SORT code in your project directory

class PlayerTracking:
    def __init__(self):
        self.next_id = 0
        self.tracked_players = {}

    def initialize_sort(self):
        # Initialize SORT tracker
        self.tracker = Sort()

    def update(self, frame, recognized_players):
        if not hasattr(self, 'tracker'):
            self.initialize_sort()

        # Use the SORT tracker to predict and match player bounding boxes
        tracks = self.tracker.update(np.array(recognized_players))
        self.update_tracked_players(tracks)
        self.remove_inactive_players()
        return self.tracked_players

    def update_tracked_players(self, tracks):
        for track in tracks:
            player_id = int(track[4])
            bbox = track[:4]
            if player_id not in self.tracked_players:
                self.tracked_players[player_id] = {
                    "bbox_history": [],
                    "frame_history": []
                }
            self.tracked_players[player_id]["bbox_history"].append(bbox)

    def remove_inactive_players(self):
        # Remove players that have been inactive for too long
        inactive_players = [player_id for player_id, player_data in self.tracked_players.items() if len(player_data["bbox_history"]) == 0]
        for player_id in inactive_players:
            del self.tracked_players[player_id]
        
    def assign_player_ids(self, recognized_players):
        new_recognized_players = []
        for player_bbox in recognized_players:
            if len(self.tracked_players) == 0:
                player_id = self.next_id
                self.next_id += 1
            else:
                player_id = self.find_closest_player(player_bbox)
                if player_id is None:
                    player_id = self.next_id
                    self.next_id += 1
            new_recognized_players.append((player_bbox, player_id))
        return new_recognized_players

    def find_closest_player(self, player_bbox):
        for player_id, player_data in self.tracked_players.items():
            last_bbox = player_data["bbox_history"][-1]
            if self.box_overlap(last_bbox, player_bbox):
                return player_id
        return None

    def box_overlap(self, bbox1, bbox2):
        x1, y1, x2, y2 = bbox1
        x3, y3, x4, y4 = bbox2
        return not (x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1)

if __name__ == "__main__":
    # Example usage:
    player_tracking_module = PlayerTracking()

    recognized_players = [
        {"bbox": [100, 100, 200, 200]},
        {"bbox": [300, 300, 400, 400]},
        {"bbox": [150, 150, 250, 250]}
    ]

    frame = np.zeros((480, 640, 3), dtype=np.uint8)  # A dummy frame for demonstration

    updated_tracked_players = player_tracking_module.update(frame, recognized_players)

    for player_id, player_data in updated_tracked_players.items():
        print(f"Player ID: {player_id}, Bounding Box History: {player_data['bbox_history']}")

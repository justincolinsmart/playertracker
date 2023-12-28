class PlayerRecognition:
    def __init__(self):
        self.players = {}
        self.next_player_id = 0

    def recognize_players(self, detected_players):
        recognized_players = []

        for player_bbox in detected_players:
            player_id = self.assign_player_id(player_bbox)
            recognized_players.append({"id": player_id, "bbox": player_bbox})

        return recognized_players

    def assign_player_id(self, player_bbox):
        for player_id, bbox in self.players.items():
            if self.overlap(player_bbox, bbox):
                return player_id

        new_player_id = self.next_player_id
        self.players[new_player_id] = player_bbox
        self.next_player_id += 1

        return new_player_id

    def overlap(self, bbox1, bbox2):
        x1, y1, x2, y2 = bbox1
        x3, y3, x4, y4 = bbox2
        return not (x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1)

if __name__ == "__main__":
    # Example usage:
    player_recognition_module = PlayerRecognition()

    detected_players = [
        (100, 100, 200, 200),
        (300, 300, 400, 400),
        (150, 150, 250, 250)
    ]

    recognized_players = player_recognition_module.recognize_players(detected_players)

    for player in recognized_players:
        print(f"Player ID: {player['id']}, Bounding Box: {player['bbox']}")

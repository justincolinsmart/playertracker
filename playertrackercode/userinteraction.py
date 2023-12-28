import tkinter as tk

class PlayerTrackingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Basketball Player Tracking")
        
        # Create and configure GUI elements
        self.label = tk.Label(root, text="Enter player's name:")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.submit_button = tk.Button(root, text="Submit", command=self.on_submit)
        self.submit_button.pack()

    def on_submit(self):
        player_name = self.entry.get()
        # Handle the user input (e.g., store the player name)

if __name__ == "__main__":
    root = tk.Tk()
    app = PlayerTrackingApp(root)
    root.mainloop()

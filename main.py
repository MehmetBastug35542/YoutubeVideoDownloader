# This file is the entry point of the application
# It initializes the GUI window and starts the Tkinter main loop

from tkinter import Tk
from src.gui import YouTubeDownloader

if __name__ == "__main__":
    root = Tk()  # Create the main window
    app = YouTubeDownloader(root)  # Initialize the custom GUI class
    root.mainloop()  # Start the Tkinter event loop
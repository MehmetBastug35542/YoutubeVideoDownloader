""" src/gui.py

This module contains the GUI for the YouTube video downloader application.
It uses Tkinter for the GUI and allows users to input a YouTube video URL,
select a save location, and choose download options.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import threading
from .logic import YtDownload
from .utils import FormatOptions


""" This class creates a GUI for downloading YouTube videos using yt-dlp.
It allows users to enter a video URL, select a save location,
choose a format and quality, and start the download process.
"""
class YouTubeDownloader:
    """ YouTubeDownloader class initializes
    the GUI components and handles user interactions.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader (yt-dlp)")
        self.root.geometry("600x380")
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(False, False)
        self.save_path = os.path.join(os.path.expanduser("~"), "Downloads")
        self.setup_styling()
        self.create_widgets()

    """ Setup the styling for the GUI components.
    This method configures the theme and styles for buttons, labels, entries, etc.
    """
    def setup_styling(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Arial", 10), padding=6)
        style.configure("TEntry", font=("Arial", 10))
        style.configure("TLabel", font=("Arial", 11), background="#f0f0f0")
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TCheckbutton", background="#f0f0f0")

    """ Create the GUI components.
    This method creates the main frame, labels, entries, buttons,
    and other widgets needed for the application.
    
    param self: The instance of the class.
    """
    def create_widgets(self):
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        ttk.Label(main_frame, text="Enter YouTube video URL:").pack(anchor="w", pady=(0, 5))
        self.url_entry = ttk.Entry(main_frame, width=60)
        self.url_entry.pack(fill=tk.X, ipady=5, pady=(0, 15))

        location_frame = ttk.Frame(main_frame)
        location_frame.pack(fill=tk.X, pady=(0, 15))

        ttk.Label(location_frame, text="Save location:").pack(side=tk.LEFT, padx=(0, 5))
        self.location_entry = ttk.Entry(location_frame, width=45)
        self.location_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.location_entry.insert(0, self.save_path)
        ttk.Button(location_frame, text="Browse...", command=self.browse_location).pack(side=tk.RIGHT, padx=(5, 0))

        filename_frame = ttk.Frame(main_frame)
        filename_frame.pack(fill=tk.X, pady=(0, 15))
        self.use_custom_filename = tk.BooleanVar(value=False)
        self.custom_filename_check = ttk.Checkbutton(
            filename_frame,
            text="Use custom filename",
            variable=self.use_custom_filename,
            command=self.toggle_filename_entry
        )
        self.custom_filename_check.pack(side=tk.LEFT, padx=(0, 5))
        self.filename_entry = ttk.Entry(filename_frame, width=40)
        self.filename_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.filename_entry.config(state="disabled")

        format_frame = ttk.Frame(main_frame)
        format_frame.pack(fill=tk.X, pady=(0, 15))
        ttk.Label(format_frame, text="Format:").pack(side=tk.LEFT, padx=(0, 5))

        self.format_var = tk.StringVar(value="mp4")
        self.format_dropdown = ttk.Combobox(format_frame, textvariable=self.format_var,
                                            values=["mp4", "mkv", "webm", "mp3 (audio only)"], state="readonly", width=15)
        self.format_dropdown.pack(side=tk.LEFT)

        self.quality_var = tk.StringVar(value="Best quality")
        ttk.Label(format_frame, text="Quality:").pack(side=tk.LEFT, padx=(15, 5))
        self.quality_dropdown = ttk.Combobox(format_frame, textvariable=self.quality_var,
                                             values=["Best quality", "720p", "480p", "360p", "Audio only"],
                                             state="readonly", width=15)
        self.quality_dropdown.pack(side=tk.LEFT)

        self.download_button = ttk.Button(main_frame, text="🎬 Download Video", command=self.start_download)
        self.download_button.pack(pady=15)

        self.status_label = ttk.Label(main_frame, text="Ready to download", font=("Arial", 10))
        self.status_label.pack(pady=(0, 10))
        self.progress = ttk.Progressbar(main_frame, orient=tk.HORIZONTAL, length=550, mode='indeterminate')
        self.progress.pack(fill=tk.X)

    """ Toggle the state of the filename entry based on the checkbox.
    This method enables or disables the filename entry field
    depending on whether the user wants to use a custom filename.
    
    param self: The instance of the class."""
    def toggle_filename_entry(self):
        self.filename_entry.config(state="normal" if self.use_custom_filename.get() else "disabled")

    """ Open a file dialog to select the save location.
    This method allows the user to browse their file system
    and select a directory where the downloaded video will be saved.
    
    param self: The instance of the class.
    """
    def browse_location(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.save_path = folder_path
            self.location_entry.delete(0, tk.END)
            self.location_entry.insert(0, folder_path)

    """ Start the download process in a separate thread.
    This method retrieves the URL and save location from the entries,
    validates them, and starts the download in a new thread
    to keep the GUI responsive.
    
    param self: The instance of the class."""
    def start_download(self):
        url = self.url_entry.get().strip()
        save_path = self.location_entry.get().strip()

        if not url:
            messagebox.showwarning("Warning", "Please enter a valid URL.")
            return
        if not save_path or not os.path.isdir(save_path):
            messagebox.showwarning("Warning", "Please select a valid save location.")
            return

        self.status_label.config(text="📥 Preparing to download...")
        self.download_button.config(state="disabled")
        self.progress.start(10)
        self.root.update()

        threading.Thread(target=self.download_thread, args=(url, save_path)).start()

    """ Download the video in a separate thread.
    This method is called by the start_download method
    and handles the actual downloading of the video.
    It uses the download_video function from the logic module
    and updates the status label and progress bar accordingly.
    
    param self: The instance of the class.
    param url: The URL of the YouTube video to download.
    param save_path: The directory where the video will be saved.
    """
    def download_thread(self, url, save_path):
        options = FormatOptions.get_options(self.format_var.get(), self.quality_var.get())
        filename = self.filename_entry.get().strip() if self.use_custom_filename.get() else None

        try:
            YtDownload.download_video(url, save_path, filename, options)
            self.status_label.config(text="✅ Download completed!")
        except Exception as e:
            self.status_label.config(text="❌ Error during download.")
            messagebox.showerror("Error", str(e))
        finally:
            self.download_button.config(state="normal")
            self.progress.stop()

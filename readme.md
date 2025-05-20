# YouTube Video Downloader (yt-dlp + Tkinter GUI)

This project provides a simple and user-friendly interface for downloading YouTube videos. It leverages the `yt-dlp` library to fetch the best-quality video or audio file and allows customization of file name, save location, format, and quality options through a `Tkinter`-based graphical user interface.


## Contents

- [YouTube Video Downloader (yt-dlp + Tkinter GUI)](#youtube-video-downloader-yt-dlp--tkinter-gui)
  - [Contents](#contents)
  - [Features](#features)
  - [Requirements](#requirements)
    - [Python Packages](#python-packages)
    - [FFmpeg Installation](#ffmpeg-installation)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Interface Overview](#interface-overview)
    - [Format and Quality Options](#format-and-quality-options)
    - [Custom Filename](#custom-filename)
    - [Download Process](#download-process)
  - [Code Structure](#code-structure)
  - [Error Handling](#error-handling)
  - [Contributing](#contributing)


## Features

- **Simple Interface**: Intuitive GUI built with Tkinter
- **Flexible Format Selection**: Download as MP4, MKV, WEBM, or audio-only MP3
- **Quality Options**: Highest quality, 720p, 480p, 360p, or audio-only
- **Custom Filename**: Option to specify a custom file name
- **Save Location**: Choose the folder where the download will be saved
- **Background Download**: Uses threading to keep the UI responsive
- **Notifications**: Informative status messages and pop-ups for success and errors


## Requirements

- Python 3.7 or higher
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- FFmpeg (for MP3 conversion)
- Tkinter (included with Python)


### Python Packages

```bash
pip install requirements.txt
```

### FFmpeg Installation

- **Windows**: Download from https://ffmpeg.org/download.html and add to PATH
- **macOS**: `brew install ffmpeg`
- **Linux**: Install via your package manager (`apt`, `yum`, `dnf`, etc.)


## Installation

1. Clone this repository:
```bash
git clone https://github.com/MehmetBastug35542/YoutubeVideoDownloader.git
cd youtube-downloader
```

2. Install the required Python packages:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```


## Usage

### Interface Overview

1. **Video URL Input**: Paste the YouTube video link you want to download.
2. **Save Location**: Select or enter the directory where the file will be saved.
3. **Custom Filename**: Enable the checkbox and type your desired file name.
4. **Format**: Choose between video (MP4, MKV, WEBM) or audio-only (MP3).
5. **Quality**: Select the resolution or audio-only option.
6. **🎬 Download Video**: Click to start the download.
7. **Status & Progress**: View preparation, download progress, and final status messages.

### Format and Quality Options

- **MP4, MKV, WEBM**: Combined video + audio output
- **MP3 (Audio)**: Audio extracted and converted to MP3 using FFmpeg
- **Best Quality**: `yt-dlp`’s default best video + audio combination
- **720p / 480p / 360p**: Restrict download to the specified resolution or lower

### Custom Filename

- When enabled, the user-provided name is used as the base file name.
- The extension is automatically appended based on the chosen format (.mp4, .mkv, .webm, .mp3).

### Download Process

1. Validate URL input and save location.
2. Disable the download button and start the progress bar.
3. Launch the download in a background thread using `threading.Thread`.
4. Build `yt-dlp` options (`format`, `postprocessors`, `outtmpl`, etc.).
5. Notify the user via pop-up dialogs on success or error.


## Code Structure

- **main.py**: Entry point of the application, defines the `YouTubeDownloader` class
- **YouTubeDownloader** class methods:
  - `setup_styling()`: Configure Tkinter theme and widget styles
  - `create_widgets()`: Create and arrange all GUI components
  - `toggle_filename_entry()`: Enable or disable the custom filename input
  - `browse_location()`: Open folder selection dialog
  - `get_format_options()`: Generate `yt-dlp` option dictionary based on UI selections
  - `start_download()`: Validate inputs and initiate the download thread
  - `download_video()`: Perform the actual download using `yt-dlp`
  - `download_complete()`, `download_failed()`: Handle post-download UI updates


## Error Handling

- **Invalid URL**: Warns the user if the URL field is empty.
- **Invalid Directory**: Alerts the user if the selected save location is not valid.
- **Download Errors**: Catches and displays errors from `yt-dlp` or network issues.


## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-new-feature`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-new-feature`).
5. Open a pull request.

Please follow clean code practices, detailed commit messages, and add tests where applicable.

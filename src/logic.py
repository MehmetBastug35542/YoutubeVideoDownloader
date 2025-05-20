from yt_dlp import YoutubeDL
import os

class YtDownload:
    @staticmethod
    def download_video(url, save_path, custom_filename=None, options=None):
        """
        Downloads the video using yt-dlp based on initialized values.
        """
        # Set the output template based on custom filename or default title
        outtmpl = os.path.join(save_path, '%(title)s.%(ext)s')
        if custom_filename:
            outtmpl = os.path.join(save_path, custom_filename + '.%(ext)s')

        options['outtmpl'] = outtmpl

        # Use YoutubeDL to download the video
        with YoutubeDL(options) as ydl:
            ydl.download([url])
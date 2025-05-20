# This class provides format and quality options for downloading
# It returns configuration settings used by yt-dlp (or youtube-dl)

class FormatOptions:
    @staticmethod
    def get_options(format_option, quality_option):
        """
        Returns the format and quality options for yt-dlp based on user selection.
        :param format_option: The format option selected by the user.
        :param quality_option: The quality option selected by the user.
        :return: A dictionary of options for yt-dlp.
        """
        # Check if the user selected audio-only download
        if format_option == "mp3 (audio only)" or quality_option == "Audio only":
            return {
                'format': 'bestaudio/best',  # Get best audio stream
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',  # Convert audio using FFmpeg
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'merge_output_format': 'mp3'  # Set output format
            }

        # Choose video format based on selected quality
        if quality_option == "Best quality":
            format_str = 'bestvideo+bestaudio/best'
        elif quality_option == "720p":
            format_str = 'bestvideo[height<=720]+bestaudio/best[height<=720]'
        elif quality_option == "480p":
            format_str = 'bestvideo[height<=480]+bestaudio/best[height<=480]'
        elif quality_option == "360p":
            format_str = 'bestvideo[height<=360]+bestaudio/best[height<=360]'
        else:
            format_str = 'bestvideo+bestaudio/best'  # Fallback to best available

        return {
            'format': format_str,  # Format string for yt-dlp
            'merge_output_format': format_option.replace(" (audio only)", "")  # Clean format name
        }

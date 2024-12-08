import yt_dlp
from pydub import AudioSegment
import os

def download_youtube_as_mp3(youtube_url, output_folder= r"C:\Important Files\Career Files\BSA\Intl Fest\2024"):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Set options for downloading only audio
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    # Download using yt_dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

# Example usage
youtube_url = "https://www.youtube.com/watch?v=shbKNuNPke0&ab_channel=HasibMamur"
download_youtube_as_mp3(youtube_url)

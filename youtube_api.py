from googleapiclient.discovery import build
import webbrowser
import time
import tkinter as tk
from tkinter import messagebox
from config import API_KEY, CHANNEL_ID

# Function to get the latest N video URLs from the channel
def get_latest_video_urls(api_key, channel_id, num_videos=5):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=num_videos,
        order="date"  # Get the latest videos
    )
    response = request.execute()

    video_urls = []
    for item in response['items']:
        video_id = item['id']['videoId']
        video_urls.append(f"https://www.youtube.com/watch?v={video_id}")
    
    return video_urls

# Function to play videos at specified intervals
def play_video_every_interval(api_key, channel_id, interval_minutes, num_videos):
    interval_seconds = interval_minutes * 60  # Convert minutes to seconds
    while True:
        video_urls = get_latest_video_urls(api_key, channel_id, num_videos)
        for video_url in video_urls:
            print(f"Playing video: {video_url}")
            webbrowser.open(video_url)
            print(f"Waiting for {interval_minutes} minutes...")
            time.sleep(interval_seconds)

# Function to start video playback from the GUI
def start_playing_videos():
    try:
        interval_minutes = float(interval_entry.get())  # Get the interval from input
        num_videos = int(num_videos_entry.get())  # Get number of videos to play

        if interval_minutes <= 0 or num_videos <= 0:
            messagebox.showerror("Invalid Input", "Please enter valid positive numbers for interval and number of videos.")
            return

        # Start the video playing process
        play_video_every_interval(API_KEY, CHANNEL_ID, interval_minutes, num_videos)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

# GUI Setup using tkinter
root = tk.Tk()
root.title("YouTube Auto-Play Scheduler")

# Label for interval input
interval_label = tk.Label(root, text="Interval (minutes):")
interval_label.pack(padx=10, pady=5)

# Entry field for interval input
interval_entry = tk.Entry(root)
interval_entry.pack(padx=10, pady=5)

# Label for number of videos input
num_videos_label = tk.Label(root, text="Number of Videos to Play:")
num_videos_label.pack(padx=10, pady=5)

# Entry field for number of videos
num_videos_entry = tk.Entry(root)
num_videos_entry.pack(padx=10, pady=5)

# Start Button
start_button = tk.Button(root, text="Start Playing Videos", command=start_playing_videos)
start_button.pack(padx=10, pady=20)

# Run the GUI loop
root.mainloop()

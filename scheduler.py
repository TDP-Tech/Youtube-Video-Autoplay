import webbrowser
import time

def play_video_every_interval(video_url, interval_minutes):
    interval_seconds = interval_minutes * 60  # Convert minutes to seconds
    while True:
        print(f"Playing video: {video_url}")
        webbrowser.open(video_url)
        print(f"Waiting for {interval_minutes} minutes...")
        time.sleep(interval_seconds)

# Example Usage
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgmnXb"  # Replace with your video URL
    interval_minutes = 30
    play_video_every_interval(video_url, interval_minutes)

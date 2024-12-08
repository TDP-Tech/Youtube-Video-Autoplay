## YouTube Auto-Play Scheduler Documentation

### Overview
The **YouTube Auto-Play Scheduler** is a Python-based application that automatically opens YouTube videos at regular intervals. You can configure the interval time (in minutes) and specify the number of latest videos to be played from a YouTube channel. The application is built with a simple graphical user interface (GUI) using the `tkinter` library for easy interaction.

The core functionality of the project is to fetch the latest videos from a given YouTube channel using the YouTube Data API, then open those videos in the web browser at a specified interval. The project is ideal for those who want to automate video viewing or streaming at regular intervals.

---

### Features
- **Fetch Latest Videos**: Fetch the latest videos from a specified YouTube channel.
- **Interval Playback**: Automatically open videos in the browser at set time intervals.
- **Graphical User Interface**: Simple and interactive GUI to input time intervals and number of videos to be played.
- **Customizable**: Users can adjust how many videos to play and how often the videos should be opened.

---

### Requirements

- Python 3.7+ 
- `google-api-python-client` (for interacting with YouTube Data API)
- `tkinter` (for GUI)
- `python-dotenv` (optional for securely storing API keys)

---

### Installation

1. Clone or download the repository to your local machine.
2. Install the required Python packages by running the following command:
   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` file, manually install the following libraries:
   ```bash
   pip install google-api-python-client tkinter python-dotenv
   ```

3. Create a `config.py` file in the root of the project with your **YouTube API Key** and **Channel ID**:
   ```python
   # config.py
   API_KEY = "your-api-key-here"
   CHANNEL_ID = "your-channel-id-here"
   ```

4. (Optional) To securely store API keys, use the `python-dotenv` library and create a `.env` file:
   ```
   API_KEY=your-api-key-here
   CHANNEL_ID=your-channel-id-here
   ```

---

### Usage

#### 1. **Running the Script**

Once everything is set up, run the script with the following command:

```bash
python youtube_auto_play.py
```

This will launch a GUI window for you to set up the interval and the number of videos to play.

#### 2. **Input Parameters**

The application will ask for two inputs:
- **Interval (minutes)**: The time in minutes between opening each video. The program will open the videos at the interval specified.
- **Number of Videos to Play**: The number of latest videos you want the program to fetch and open.

For example, if you want to open 5 videos every 30 minutes, you can input:
- Interval: `30`
- Number of Videos to Play: `5`

#### 3. **How it Works**

- The program uses the **YouTube Data API** to fetch the latest videos from the given channel.
- It will open the video URLs in the default web browser.
- After opening a video, the program waits for the specified time interval (e.g., 30 minutes) before opening the next video.

#### 4. **Graphical User Interface (GUI)**

The GUI allows you to interact with the program easily:
- **Interval (minutes)**: Input the number of minutes to wait between each video.
- **Number of Videos to Play**: Input how many latest videos to fetch and play.
- **Start Button**: Click to start playing videos at the specified intervals.

---

### Code Structure

The project consists of the following key files:

1. **`youtube_auto_play.py`**: Main script that handles video playback, API calls, and GUI interaction.
   
   - `get_latest_video_urls(api_key, channel_id, num_videos)`: Fetches the latest `num_videos` from the YouTube channel.
   - `play_video_every_interval(api_key, channel_id, interval_minutes, num_videos)`: Opens the videos in the web browser at the given interval.
   - `start_playing_videos()`: The function triggered by the GUI to start playing videos.

2. **`config.py`**: Stores the API key and channel ID for the YouTube Data API.

3. **`requirements.txt`**: Lists the dependencies required for the project:
   ```
   google-api-python-client
   python-dotenv
   tkinter
   ```

4. **`README.md`**: This file, which explains the project setup, usage, and requirements.

---

### Example Usage

Here is an example of how the script works:

1. **Launch the application** by running `python youtube_auto_play.py`.

2. **Input Example**:
   - **Interval (minutes)**: `30` (This will play a video every 30 minutes).
   - **Number of Videos to Play**: `3` (This will fetch and play the 3 most recent videos from the channel).

3. **Output**: 
   - The program will automatically open the 3 most recent videos in the browser, one at a time, waiting for the specified interval before opening the next video.

---

### Troubleshooting

- **API Key Error**: If you see an error related to the API key, make sure the API key is correctly set in the `config.py` file and that the API key has proper permissions to access YouTube Data API v3.
- **Invalid Channel ID**: Ensure that the channel ID is correct. The format for channel IDs typically starts with `UC` followed by a series of alphanumeric characters (e.g., `UCXy7R3lG0GZy0a8Xp1X5P0Q`).
- **Web Browser Issues**: If the browser does not open automatically, ensure that the default browser is set up correctly on your machine.

---

### Contributing

If you'd like to contribute to the project, feel free to fork the repository, make your changes, and submit a pull request. Please ensure that you follow the code style and include tests for any new features or fixes.

---

### License

This project is licensed under the MIT License. See the LICENSE file for more information.

---

Let me know if you need any adjustments to the documentation!

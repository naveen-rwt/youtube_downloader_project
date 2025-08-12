# YouTube Downloader Flask App

A simple Flask web app to download YouTube videos using yt-dlp.

## Features

- Download single YouTube videos (no playlists)
- Downloads best available video and audio merged into MP4
- Simple web interface
- Handles URL cleaning to avoid playlist downloads
- Uses ffmpeg for merging video and audio streams

## Requirements

- Python 3.7+
- Flask
- yt-dlp
- ffmpeg installed and available in system PATH

## Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   
2.Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

3.Install dependencies:

pip install -r requirements.txt

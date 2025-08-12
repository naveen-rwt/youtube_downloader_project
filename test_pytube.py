from pytube import YouTube

url = 'https://www.youtube.com/watch?v=FudfVyYWNxQ'

try:
    yt = YouTube(url)
    print(f"Title: {yt.title}")
except Exception as e:
    print(f"Error: {e}")

from flask import Flask, render_template, request, jsonify, send_file
import yt_dlp
import os
from urllib.parse import urlparse, parse_qs, urlunparse

app = Flask(__name__)

# Directory where videos will be saved
DOWNLOAD_DIR = 'downloads'
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def clean_url(url):
    """Remove playlist & keep only video URL."""
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    if 'v' in query:
        new_query = f"v={query['v'][0]}"
        return urlunparse((parsed.scheme, parsed.netloc, parsed.path, '', new_query, ''))
    return url  # fallback

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    try:
        data = request.get_json(force=True)
        original_url = data.get('url')
        if not original_url:
            return jsonify({'success': False, 'error': 'No URL provided'}), 400

        # Clean the URL to avoid downloading playlists
        url = clean_url(original_url)

        # yt-dlp options
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'quiet': True,
            'no_warnings': True,
            'ignoreerrors': True,
            'noplaylist': True  # <-- Ensure only one video is downloaded
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            if not info:
                return jsonify({'success': False, 'error': 'Could not download video'}), 400

            # Get final filename
            filename = ydl.prepare_filename(info)
            filename = os.path.splitext(os.path.basename(filename))[0] + '.mp4'

            return jsonify({
                'success': True,
                'filename': filename,
                'title': info.get('title', 'Downloaded Video')
            })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/video/<filename>')
def serve_video(filename):
    path = os.path.join(DOWNLOAD_DIR, filename)
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True)

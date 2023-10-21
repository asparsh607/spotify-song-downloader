import zipfile
import io
from flask import Flask, request, render_template, redirect, send_file
from song_download import download_track, download_playlist
from extracting_song import get_song_list
from song_accumulator import song_dispatcher, song_terminator


# creating the app instance for the backend
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/single")
def single_track():
    return render_template("single_track.html")

@app.route("/playlist")
def playlist():
    return render_template("playlist.html")

@app.route('/download')
def download():
    # Create an in-memory binary stream
    memory_file = io.BytesIO()
    
    # Create a ZIP file in the memory stream
    with zipfile.ZipFile(memory_file, 'w') as zf:
        # Add each file to the ZIP file
        mp4_list = song_dispatcher()
        for songs in mp4_list:
            zf.write(songs)
    
    # Set the stream position to the start of the file
    memory_file.seek(0)
    song_terminator(mp4_list)
    
    # Send the ZIP file to the client
    return send_file(memory_file, download_name='Attachment.zip', as_attachment=True)


# function to get the single track link variable name from Spotify_song_downloader\templates\single_track.html
@app.route("/single_track_name", methods = ["GET", "POST"])
def single_track_name():
    if request.method == "POST":
        download_track(song_name = request.form.get("link_of_song"))
    return render_template("thanks.html")

#function to get playlist link variable name from Spotify_song_downloader\templates\playlist.html
@app.route("/playlist_name", methods = ["GET", "POST"])
def playlist_name():
    if request.method == "POST":
        result_list = get_song_list(playlist_link=request.form.get("link_of_playlist"))
        download_playlist(search_list=result_list)
        
    return render_template("thanks.html")



if __name__ == "__main__":
    app.run(debug=True)

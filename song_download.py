from pytube import YouTube, Search

def download_track(song_name):
    s = Search(song_name)
    result = s.results[0].video_id
    yt = YouTube(f"http://youtube.com/watch?v={result}")
    track = yt.streams.filter(only_audio=True)[0]
    track.download()

def download_playlist(search_list):
    for search in search_list:
        s = Search(search)
        result = s.results[0].video_id
        yt = YouTube(f"http://youtube.com/watch?v={result}")
        track = yt.streams.filter(only_audio=True)[0]
        track.download()
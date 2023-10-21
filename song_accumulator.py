import os, re

def song_dispatcher():
    path = "."
    dir_list = os.listdir(path)

    mylist = dir_list
    r = re.compile(".*mp4")
    mp4_list = list(filter(r.match, mylist))
    return mp4_list

def song_terminator(mp4_list):
    for songs in mp4_list:
        print(songs)
        os.remove(songs)
    
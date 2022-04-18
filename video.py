from pytube import Playlist

try:
    playlist = Playlist('https://www.youtube.com/playlist?list=PLOLrQ9Pn6caw0PjVwymNc64NkUNbZlhFw')
    for v in playlist.videos:
        print(v.author)
        print(v.keywords)
        print()
except Exception as e:
    print(e)

"""A video playlist class."""


from typing import Sequence


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self, playlist_title: str):
        self._title = playlist_title
        self._videos = []

    def add_video(self, video_id):
        self._videos.append(video_id)
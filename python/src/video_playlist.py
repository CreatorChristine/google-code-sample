"""A video playlist class."""


from typing import Sequence


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self, playlist_title: str, playlist_id: str, video_ids: Sequence[str]):
        self._title = playlist_title
        self._playlist_id = playlist_id
        self._videos = video_ids
        pass

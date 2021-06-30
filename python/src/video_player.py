"""A video player class."""

from os import getloadavg
from .video_library import VideoLibrary
import secrets

class VideoPlayer:
    """A class used to represent a Video Player."""
    global current_video
    current_video = None

    def __init__(self):
        self._video_library = VideoLibrary()
        global current_video
        current_video = None

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        all_videos = list(self._video_library.get_all_videos())
        videos = []
        print("Here's a list of all available videos:")
        for i in all_videos:
            joined_tuple = list(map("".join, i.tags))
            video_info = str(i.title) + " (" + str(i.video_id) + ") " + '[' + str(' '.join(joined_tuple)) + ']'
            videos.append(video_info)
        videos.sort()
        for i in videos:
            print(i)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        global current_video
        video = self._video_library.get_video(video_id)
        if video == None:
            error = "Cannot play video: Video does not exist"
            print(error)
        elif video and current_video == None:
            playing = "Playing video: " + str(video.title)
            current_video = video
            current_video.status = "playing"
            print(playing)
        elif video and current_video != None and current_video.status != "paused":
            stopping = "Stopping video: " + str(current_video.title)
            current_video.status = "stopping"
            print(stopping)
            current_video = video
            current_video.status = "playing"
            playing = "Playing video: " + str(video.title)
            print(playing)
        elif video and current_video != None and current_video.status == "paused":
            stopping = "Stopping video: " + str(current_video.title)
            print(stopping)
            current_video = video
            current_video.status = "playing"
            playing = "Playing video: " + str(video.title)
            print(playing)



        # print("play_video needs implementation")

    def stop_video(self):
        """Stops the current video."""
        global current_video
        if current_video == None:
            error = "Cannot stop video: No video is currently playing"
            print(error)
        elif current_video.status == "playing" or current_video.status == "continuing" or current_video.status == "paused":
            print('Stopping video: ' + current_video.title)
            current_video = None

        # print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""

        all_videos = list(self._video_library.get_all_videos())

        global current_video
        if current_video:
            print(f"Stopping video: {current_video.title}") 
            current_video.status = "stopped"
        current_video = secrets.choice(all_videos)
        current_video.status = "playing"
        print(f"Playing video: {current_video.title}")

        if len(all_videos) == 0:
            print("No videos available")


        # print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        global current_video
        if current_video == None or current_video.status != "playing" and current_video.status != "paused":
            print(f"Cannot pause video: No video is currently playing")
        elif current_video.status == "playing":
            current_video.status = "paused"
            print(f"Pausing video: {current_video.title}")
        elif current_video.status == "paused":
            print(f"Video already paused: {current_video.title}")



        # print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""
        if current_video == None:
            print(f'Cannot continue video: No video is currently playing')
        elif current_video.status == "paused":
            current_video.status = "continuing"
            print(f'Continuing video: {current_video.title}')
        elif current_video.status == "continuing" or current_video.status == "playing":
            print(f'Cannot continue video: Video is not paused')

        # print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        if current_video != None:
            joined_tuple = list(map("".join, current_video.tags))
            new_tags = ' '.join(joined_tuple)
            if current_video.status != "paused":
                print(f"Currently playing: {current_video.title} ({current_video.video_id}) [{new_tags}]")
            if current_video.status == "paused":
                print(f"Currently playing: {current_video.title} ({current_video.video_id}) [{new_tags}] - PAUSED")
        else:
            print("No video is currently playing")

        # print("show_playing needs implementation")
    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")

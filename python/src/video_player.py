from .video_library import VideoLibrary
from .algorithms import title_insertion_sort
from .playlist import Playlist

import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._video_playing = None

        self._playlists = []

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        all_sorted_videos = title_insertion_sort(self._video_library.get_all_videos())
        print("Here's a list of all available videos: ")

        for video in all_sorted_videos:
            # Unpack the video object
            video_title = video.title
            video_id = video.video_id
            video_tags = " ".join(video.tags)

            print(f"  {video_title} ({video_id}) [{video_tags}]")

    def play_video(self, video_id):
        """Plays the respective video.
ºº
        Args:
            video_id: The video_id to be played.
        """

        next_video = self._video_library.get_video(video_id)

        if next_video is None:
            print("Cannot play video: Video does not exist")

        else:

            # If class field is a truthy value (ie. not Null)
            if self._video_playing:
                print(f"Stopping video: {self._video_playing.get('video').title}")

            print(f"Playing video: {next_video.title}")
            # Update video currently playing
            self._video_playing = {
                "video": next_video,
                "paused": False
            }

    def stop_video(self):
        """Stops the current video."""

        if self._video_playing is None:
            print("Cannot stop video: No video is currently playing")

        else:
            print(f"Stopping video: {self._video_playing.get('video').title}")
            self._video_playing = None  # Update class field to represent video stopping

    def play_random_video(self):
        """Plays a random video from the video library."""

        if self._video_playing:
            print(f"Stopping video: {self._video_playing.get('video').title}")

        random_video = random.choice(self._video_library.get_all_videos())

        print(f"Playing video: {str(random_video.title)}")
        # Update video that is currently playing
        self._video_playing = {
            "video": random_video,
            "paused": False
        }

    def pause_video(self):
        """Pauses the current video."""

        if self._video_playing:

            if self._video_playing.get('paused'):
                print(f"Video already paused: {self._video_playing.get('video').title}")

            else:
                print(f"Pausing video: {self._video_playing.get('video').title}")
                self._video_playing['paused'] = True

        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""

        if self._video_playing:

            if not self._video_playing.get('paused'):
                print("Cannot continue video: Video is not paused")

            else:
                print(f"Continuing video: {self._video_playing.get('video').title}")
                self._video_playing['paused'] = False  # Update video paused state to False

        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""

        if self._video_playing:

            video_object = self._video_playing.get('video')
            video_title = video_object.title
            video_id = video_object.video_id
            video_tags = " ".join(video_object.tags)

            video_paused = " - PAUSED" if self._video_playing.get('paused') else ""

            print(f"Currently playing: {video_title} ({video_id}) [{video_tags}]{video_paused}")

        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        playlist_name = "_".join(playlist_name.split(" "))  # If there are any spaces in name, add _

        # Check playlist doesn't already exist, transform to uppercase because case-insensitive
        if playlist_name.upper() in [playlist.title.upper() for playlist in self._playlists]:
            print("Cannot create playlist: A playlist with the same name already exists")

        else:
            new_playlist = Playlist(playlist_name)
            self._playlists.append(new_playlist)

    def select_playlist(self, playlist_name):
        """Returns playlist in video player with same name as argument"""
        if playlist_name.upper() in [playlist.title.upper() for playlist in self._playlists]:
            return [playlist for playlist in self._playlists
                    if playlist.title.upper() == playlist_name.upper()][0]

        else:
            return None

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """

        if playlist_name.upper() not in [playlist.title.upper() for playlist in self._playlists]:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")

        else:
            selected_playlist = self.select_playlist(playlist_name)
            selected_playlist.addVideo(playlist_name, self._video_library.get_all_videos(), video_id)

    def show_all_playlists(self):
        """Display all playlists."""

        if len(self._playlists) == 0:
            print("No playlists exist yet")

        else:
            print("Showing all playlists:")

            sorted_playlists = title_insertion_sort(self._playlists)
            for playlist in sorted_playlists:
                print(f"  {playlist.title}")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        if playlist_name.upper() not in [playlist.title.upper() for playlist in self._playlists]:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")

        else:
            selected_playlist = self.select_playlist(playlist_name)
            selected_playlist.showPlaylist(playlist_name)

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """

        selected_playlist = self.select_playlist(playlist_name)
        if selected_playlist is None:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")

        else:
            selected_playlist.removeVideo(playlist_name, self._video_library.get_all_videos(), video_id)

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

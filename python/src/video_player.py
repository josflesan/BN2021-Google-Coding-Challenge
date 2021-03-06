from .video_library import VideoLibrary
from .algorithms import title_insertion_sort, title_linear_search, tag_linear_search
from .playlist import Playlist

import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._video_playing = None

        self._playlists = []

    def number_of_videos(self):
        """Prints number of videos in library"""
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
            video_flag = "" if not video.getFlag()['set'] else f" - FLAGGED (reason: {video.getFlag()['reason']})"

            print(f"  {video_title} ({video_id}) [{video_tags}]{video_flag}")

    def play_video(self, video_id):
        """Plays the respective video.
ºº
        Args:
            video_id: The video_id to be played.
        """

        next_video = self._video_library.get_video(video_id)

        if next_video is None:
            print("Cannot play video: Video does not exist")

        elif next_video.getFlag()["set"]:
            print(f"Cannot play video: Video is currently flagged (reason: {next_video.getFlag()['reason']})")

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

        possible_videos = [video for video in self._video_library.get_all_videos() if not video.getFlag()['set']]
        if len(possible_videos) == 0:
            print("No videos available")

        else:
            random_video = random.choice(possible_videos)

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

        selected_playlist = self.select_playlist(playlist_name)
        if selected_playlist is None:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")

        else:
            selected_playlist.clear(playlist_name)

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        selected_playlist = self.select_playlist(playlist_name)
        if selected_playlist is None:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")

        else:
            self._playlists.remove(selected_playlist)
            print(f"Deleted playlist: {playlist_name}")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """

        existing_videos = self._video_library.get_all_videos()
        unsorted_search_results = title_linear_search(existing_videos, search_term)
        sorted_search_results = title_insertion_sort(unsorted_search_results)

        if len(sorted_search_results) == 0:
            print(f"No search results for {search_term}")

        else:
            print(f"Here are the results for {search_term}:")
            for i in range(0, len(sorted_search_results)):
                result = sorted_search_results[i]
                print(f"  {i+1}) {result.title} ({result.video_id}) [{' '.join(result.tags)}]")

            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            video_to_play = input()

            if video_to_play in [str(num) for num in range(1, len(sorted_search_results)+1)]:
                self.play_video(sorted_search_results[int(video_to_play)-1].video_id)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """

        existing_videos = self._video_library.get_all_videos()
        unsorted_search_results = tag_linear_search(existing_videos, video_tag)
        sorted_search_results = title_insertion_sort(unsorted_search_results)

        if len(sorted_search_results) == 0:
            print(f"No search results for {video_tag}")

        else:
            print(f"Here are the results for {video_tag}:")
            for i in range(0, len(sorted_search_results)):
                result = sorted_search_results[i]
                print(f"  {i + 1}) {result.title} ({result.video_id}) [{' '.join(result.tags)}]")

            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            video_to_play = input()

            if video_to_play in [str(num) for num in range(1, len(sorted_search_results)+1)]:
                self.play_video(sorted_search_results[int(video_to_play)-1].video_id)

    def flag_video(self, video_id, flag_reason="Not supplied"):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """

        if video_id not in [video.video_id for video in self._video_library.get_all_videos()]:
            print(f"Cannot flag video: Video does not exist")

        else:
            selected_video = [video for video in self._video_library.get_all_videos() if video.video_id == video_id][0]

            if selected_video.getFlag()["set"]:
                print(f"Cannot flag video: Video is already flagged")

            else:
                selected_video.setFlag(flag_reason)

                if self._video_playing is not None:
                    if selected_video.video_id == self._video_playing['video'].video_id:
                        self.stop_video()

                print(f"Successfully flagged video: {selected_video.title} (reason: {flag_reason})")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """

        if video_id not in [video.video_id for video in self._video_library.get_all_videos()]:
            print(f"Cannot remove flag from video: Video does not exist")

        else:
            selected_video = [video for video in self._video_library.get_all_videos() if video.video_id == video_id][0]

            if not selected_video.getFlag()['set']:
                print(f"Cannot remove flag from video: Video is not flagged")

            else:
                selected_video.unFlag()
                print(f"Successfully removed flag from video: {selected_video.title}")

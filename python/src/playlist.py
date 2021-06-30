"""A playlist class"""


class Playlist:

    def __init__(self, name):
        """Playlist constructor"""
        self._videos = []
        self._video_ids = []
        self._name = name

        print(f"Successfully created new playlist: {name}")

    @property
    def title(self):
        """Returns playlist name"""
        return self._name

    @property
    def getVideos(self):
        """Returns list of videos in playlist"""
        return self._videos

    @property
    def getVideoIDs(self):
        """Returns list of video IDs"""
        return self._video_ids

    def addVideo(self, playlist_name, library, video_id):
        """Adds a video to the playlist"""

        existing_videos = [video.video_id for video in library]
        if video_id not in existing_videos:
            print(f"Cannot add video to {playlist_name}: Video does not exist")

        else:

            new_video = [video for video in library if (video.video_id == video_id)][0]

            if new_video.getFlag()["set"]:
                print(
                    f"Cannot add video to {playlist_name}: Video is currently flagged (reason: {new_video.getFlag()['reason']})"
                )

            elif new_video.video_id in self.getVideoIDs:
                print(f"Cannot add video to {playlist_name}: Video already added")

            else:
                print(f"Added video to {playlist_name}: {new_video.title}")
                self._videos.append(new_video)
                self._video_ids.append(video_id)

    def removeVideo(self, playlist_name, library, video_id):
        """Removes a video from the playlist"""

        existing_videos = [video.video_id for video in library]

        if video_id not in existing_videos:
            print(f"Cannot remove video from {playlist_name}: Video does not exist")

        elif video_id not in self.getVideoIDs:
            print(f"Cannot remove video from {playlist_name}: Video is not in playlist")

        else:
            removed_video = [video for video in self._videos if video.video_id == video_id][0]

            # Update the video list to exclude removed video
            self._videos = [video for video in self._videos if video.video_id != video_id]
            self._video_ids.remove(video_id)
            print(f"Removed video from {playlist_name}: {removed_video.title}")

    def showPlaylist(self, playlist_name):
        print(f"Showing playlist: {playlist_name}")

        if len(self.getVideos) == 0:
            print("  No videos here yet")

        else:
            for video in self.getVideos:
                video_flag = "" if not video.getFlag()['set'] else f" - FLAGGED (reason: {video.getFlag()['reason']})"
                print(f"  {video.title} ({video.video_id}) [{' '.join(video.tags)}]{video_flag}")

    def clear(self, playlist_name):
        self._videos = []
        self._video_ids = []
        print(f"Successfully removed all videos from {playlist_name}")

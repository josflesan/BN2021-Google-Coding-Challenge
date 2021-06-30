"""A playlist class"""


class Playlist:

    def __init__(self, name):
        """Playlist constructor"""
        self._videos = []
        self._video_ids = []
        self._name = name

        print(f"Successfully created new playlist: {name}")

    @property
    def getName(self):
        """Returns playlist name"""
        return self._name

    @property
    def getVideoIDs(self):
        """Returns list of video IDs"""
        return self._video_ids

    def add(self, playlist_name, library, video_id):
        """Adds a video to the playlist"""

        existing_videos = [video.video_id for video in library]
        if video_id not in existing_videos:
            print(f"Cannot add video to {playlist_name}: Video does not exist")

        else:

            new_video = [video for video in library if (video.video_id == video_id)][0]

            if new_video.video_id in self.getVideoIDs:
                print(f"Cannot add video to {playlist_name}: Video already added")

            self._videos.append(new_video)
            self._video_ids.append(video_id)




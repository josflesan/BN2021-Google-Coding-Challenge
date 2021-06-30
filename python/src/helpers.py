"""File containing helper functions"""


def checkVideoExists(playlist_name, library, video_id):
    existing_videos = [video.video_id for video in library]
    if video_id not in existing_videos:
        print(f"Cannot add video to {playlist_name}: Video does not exist")





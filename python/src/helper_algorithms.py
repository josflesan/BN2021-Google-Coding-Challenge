"""A set of helper functions implementing useful algorithms."""

from .video_library import VideoLibrary


def title_insertion_sort(unsorted_object: VideoLibrary):
    """Returns list of video objects sorted by title"""

    all_videos = unsorted_object.get_all_videos()

    for i in range(1, len(all_videos)):
        key = all_videos[i]
        j = i - 1

        while j >= 0 and str(all_videos[j].title) > str(key.title):
            # Shift elements upwards
            all_videos[j+1] = all_videos[j]
            j -= 1

        # Insert key into position
        all_videos[j + 1] = key

    return all_videos

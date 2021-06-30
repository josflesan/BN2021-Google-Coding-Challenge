"""A set of helper functions implementing useful algorithms."""


def title_insertion_sort(unsorted_object):
    """Returns list of video objects sorted by title"""

    all_videos = unsorted_object

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


def title_linear_search(video_list, pattern):
    search_results = []

    for video in video_list:
        if pattern.upper() in video.title.upper() and not video.getFlag()['set']:
            search_results.append(video)

    return search_results


def tag_linear_search(video_list, tag):
    search_results = []

    for video in video_list:
        if tag.upper() in [tag.upper() for tag in video.tags] and \
                not video.getFlag()['set']:
            search_results.append(video)

    return search_results


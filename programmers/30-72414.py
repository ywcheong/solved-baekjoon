def timestamp_to_key(timestamp: str):
    hour = int(timestamp[:2])
    minute = int(timestamp[3:5])
    second = int(timestamp[6:8])
    return 60 * (60 * hour + minute) + second


def key_to_timestamp(key) -> str:
    hour = (key // 3600) % 60
    minute = (key // 60) % 60
    second = (key // 1) % 60
    return f"{hour:02}:{minute:02}:{second:02}"


def solution(video_length_timestamp, ad_length_timestamp, timestamp_log_list):
    video_length = timestamp_to_key(video_length_timestamp)
    ad_length = timestamp_to_key(ad_length_timestamp)
    # at time t:00, + viewer_change[t] occurs
    # note that we want [start, end)
    viewer_change = [0] * (video_length + 1)
    for timestamp_log in timestamp_log_list:
        start_key = timestamp_to_key(timestamp_log[:8])
        end_key = timestamp_to_key(timestamp_log[9:])

        viewer_change[start_key] += 1
        viewer_change[end_key] -= 1

    viewer_total = [0] * (video_length + 1)
    viewer_total[0] = viewer_change[0]
    for i in range(1, video_length + 1):
        viewer_total[i] = viewer_total[i - 1] + viewer_change[i]

    start_key, end_key, viewer = 0, 0, 0
    while end_key < ad_length:
        viewer += viewer_total[end_key]
        end_key += 1
    max_start_key, max_viewer = 0, viewer

    while end_key <= video_length:
        viewer += -viewer_total[start_key] + viewer_total[end_key]
        start_key, end_key = start_key + 1, end_key + 1

        if viewer > max_viewer:
            max_start_key, max_viewer = start_key, viewer
        
    return key_to_timestamp(max_start_key)
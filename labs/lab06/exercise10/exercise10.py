def get_unique_attendees(attendance_logs):
    """Extract set of all unique attendee IDs."""
    attendees = set()
    for attendee_id, event_name in attendance_logs:
        attendees.add(attendee_id)
    return attendees


def count_unique_events(attendance_logs, attendee_id):
    """Count how many unique events this attendee attended."""
    events = set()
    for att_id, event_name in attendance_logs:
        if att_id == attendee_id:
            events.add(event_name)

    return len(events)


def filter_by_threshold(attendees, attendance_logs, min_events):
    """Return sorted list of attendees who attended >= min_events."""
    qualified = []
    for attendee_id in attendees:
        if count_unique_events(attendance_logs, attendee_id) >= min_events:
            qualified.append(attendee_id)

    return sorted(qualified)


def find_frequent_attendees(attendance_logs, min_events):
    """Find attendees who attended at least min_events unique events."""
    attendees = get_unique_attendees(attendance_logs)
    return filter_by_threshold(attendees, attendance_logs, min_events)

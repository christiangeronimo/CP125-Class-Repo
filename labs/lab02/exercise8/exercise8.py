def calculate_bounce_height(current_height):
    """Calculate next bounce height (80% of current)."""
    return current_height * 0.8


def is_ball_stopped(height):
    """Return True if height < 1, False otherwise."""
    return height < 1


def simulate_bouncing_ball(start_height):
    bounce_count = 0
    total_distance = start_height
    current_height = start_height

    while not is_ball_stopped(current_height):
        current_height = calculate_bounce_height(current_height)
        bounce_count += 1

        if not is_ball_stopped(current_height):
            total_distance += 2 * current_height

    return bounce_count, total_distance




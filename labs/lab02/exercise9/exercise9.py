# Lab 02 Exercise 9: Level Up Calculator

def calculate_xp_required(current_level):
    """Return XP needed to level up (level * 100)."""
    return current_level * 100


def can_level_up(xp_remaining, xp_required):
    """Return True if xp_remaining >= xp_required."""
    return xp_remaining >= xp_required


def simulate_leveling(total_xp):
    """
    Simulate leveling with given XP.
    Returns: (final_level, remaining_xp)
    """
    level = 1
    xp_remaining = total_xp
    xp_required = calculate_xp_required(level)
    while can_level_up(xp_remaining, xp_required):
        xp_remaining -= xp_required
        level += 1
        xp_required = calculate_xp_required(level)

    return level, xp_remaining


# Test your code here
print("Testing Level Up Calculator...")

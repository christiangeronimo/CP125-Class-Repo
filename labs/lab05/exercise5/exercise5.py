
def clean_sessions(pool, sessions, dead_servers):
    """
    Verify dead servers in pool, remove their sessions, and return sorted list.
    """

    valid_dead = []
    for server in dead_servers:
        if server in pool:
            valid_dead.append(server)

    remaining_sessions = []
    for session in sessions:
        server_id = session[0]

        if server_id not in valid_dead:
            remaining_sessions.append(session)

    remaining_sessions.sort() 

    return remaining_sessions




# Test
pool = ("srv-A", "srv-B", "srv-C", "srv-D")
sessions = [("srv-B", "cli-1"), ("srv-A", "cli-2"), ("srv-C", "cli-3"),
            ("srv-B", "cli-4"), ("srv-D", "cli-5")]
dead = ["srv-B", "srv-D"]

result = clean_sessions(pool, sessions, dead)
print(f"Cleaned Sessions: {result}")
# Expected: [('srv-A', 'cli-2'), ('srv-C', 'cli-3')]

def synchronize_databases(legacy_list, modern_set, blacklist):
    cleaned_legacy = set()
    for record_id,email in legacy_list:
        if email not in blacklist:
            cleaned_legacy.add(record_id)

    lost_id = cleaned_legacy - modern_set
    ghost_id = modern_set - cleaned_legacy

    return lost_id ,ghost_id

legacy = [(1, "a@b.com"), (2, "c@d.com")]
modern = {1, 3}
lost, ghost = synchronize_databases(legacy, modern, set())


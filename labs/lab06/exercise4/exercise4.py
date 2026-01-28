def synchronize_databases(legacy_list, modern_set, blacklist):
    cleaned_legacy = set()
    for record_id,email in legacy_list:
        if email not in blacklist:
            cleaned_legacy.add(record_id)

    lost_id = cleaned_legacy - modern_set
    ghost_id = modern_set - cleaned_legacy

    return lost_id ,ghost_id




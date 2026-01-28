def audit_blocklists(list_a, list_b, list_c):
    universal = list_a & list_b & list_c
    redundant = (list_a & list_b) | (list_a & list_c) | (list_b & list_c)
    unique_A = list_a - list_b - list_c

    return universal,redundant,unique_A
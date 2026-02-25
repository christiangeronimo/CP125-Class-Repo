def apply_upgrade(current, upgrade):
    # Create a copy so original is not modified
    result = dict(current)
    
    for permission, level in upgrade.items():
        if permission in result:
            # Only update if upgrade level is higher
            if level > result[permission]:
                result[permission] = level
        else:
            # Add new permission
            result[permission] = level
    
    return result


current = {"read": 2, "write": 1, "admin": 0}
upgrade = {"read": 1, "write": 3, "execute": 2}

result = apply_upgrade(current, upgrade)

print(result)
print(current)   # Should be unchanged
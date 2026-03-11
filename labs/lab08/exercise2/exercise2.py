def merge_lists(file1, file2, output_file):
    """
    Merge two lists of names, remove duplicates, and sort.

    Args:
        file1: path to first list file
        file2: path to second list file
        output_file: path to output file

    Returns:
        int: count of unique names
    """

    f = open(file1, 'r') 
    list1 = f.readlines()

    
    g = open(file2, 'r')
    list2 = g.readlines()

    unique_names = []


    for name in list1 + list2:
        if name not in unique_names:  
            unique_names.append(name)

    unique_names.sort()

    merged = open(output_file, 'w') 
    merged.writelines(unique_names)

    return len(unique_names)


# Test your code here
result = merge_lists(
    "labs/lab08/exercise2/data/list1.txt",
    "labs/lab08/exercise2/data/list2.txt",
    "labs/lab08/exercise2/data/merged.txt"
)

print(f"Unique names: {result}")
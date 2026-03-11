def merge_lists(file1, file2, output_file):

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
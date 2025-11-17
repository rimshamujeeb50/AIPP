# Optimized version using Python sets

def find_common(a, b):
    # Use set intersection to get common elements
    return list(set(a) & set(b))

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_elements = find_common(list1, list2)
print("Common elements:", common_elements)

def binary_search(arr, target):
    """
    Performs binary search on a sorted array to find the index of the target value.

    Args:
        arr (list): The sorted array to search.
        target (int): The value to search for.

    Returns:
        int: The index of the target value if found, -1 otherwise.
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = binary_search(arr, target)

    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")

import random


def quickselect(arr, k):
    """
    Quickselect algorithm to find the k-th smallest element in an array.

    Parameters:
        arr (list): The input array.
        k (int): The position of the smallest element to find (1-based).

    Returns:
        int: The k-th smallest element in the array.
    """
    if len(arr) == 1:  # Base case: only one element
        return arr[0]

    # Choose a random pivot
    pivot = random.choice(arr)

    # Partition the array
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Decide the next step based on k
    if k <= len(left):
        # k-th element is in the left partition
        return quickselect(left, k)
    elif k <= len(left) + len(mid):
        # k-th element is in the pivot group
        return mid[0]
    else:
        # k-th element is in the right partition
        return quickselect(right, k - len(left) - len(mid))


# Example Usage:
arr = [3, 2, 1, 5, 4]
k = 3
print(f"The {k}-th smallest element is: {quickselect(arr, k)}")

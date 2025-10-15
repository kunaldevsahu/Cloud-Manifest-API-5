"""
binary_search.py

This module implements both iterative and recursive versions of the binary search algorithm.
Binary search is an efficient algorithm for searching a sorted array by repeatedly dividing
the search interval in half. It has a time complexity of O(log n).

Features:
- Iterative implementation
- Recursive implementation
- Search for exact matches
- Find insertion position for new elements
"""

def binary_search_iterative(arr, target):
    """
    Iterative implementation of binary search.
    
    Args:
        arr: A sorted list of comparable elements
        target: The value to search for
    
    Returns:
        int: Index of target if found, -1 if not found
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

def binary_search_recursive(arr, target, left=None, right=None):
    """
    Recursive implementation of binary search.
    
    Args:
        arr: A sorted list of comparable elements
        target: The value to search for
        left: Starting index for search range (optional)
        right: Ending index for search range (optional)
    
    Returns:
        int: Index of target if found, -1 if not found
    """
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
        
    if left > right:
        return -1
        
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

def find_insertion_position(arr, target):
    """
    Find the position where target should be inserted to maintain sorted order.
    
    Args:
        arr: A sorted list of comparable elements
        target: The value to find insertion position for
    
    Returns:
        int: Index where target should be inserted
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
            
    return left

def demo():
    """
    Demonstration of binary search implementations
    """
    # Test array
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    
    # Test iterative search
    target = 7
    result = binary_search_iterative(arr, target)
    print(f"Iterative search: {target} found at index {result}")
    
    # Test recursive search
    target = 15
    result = binary_search_recursive(arr, target)
    print(f"Recursive search: {target} found at index {result}")
    
    # Test searching for missing element
    target = 10
    result = binary_search_iterative(arr, target)
    print(f"Searching for {target} (not in array): {result}")
    
    # Test insertion position
    pos = find_insertion_position(arr, target)
    print(f"Insertion position for {target}: {pos}")

if __name__ == "__main__":
    demo()

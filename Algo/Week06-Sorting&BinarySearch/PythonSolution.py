# Week 6 Problems: Sorting & Binary Search

# -------------------------------------------------------------
# I. Binary Search (Easy) - LeetCode #704 | Binary Search
# -------------------------------------------------------------

# Importance: ⭐⭐⭐⭐⭐ (5/5)
# - Basic and frequently asked problem for Binary Search.
# - Essential to learn efficient searching algorithms.

# Goal:
# - Find the target number in a sorted array and return its index.
# - If not found, return -1.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # Initialize search range

    while left <= right:  # Continue until the range is valid
        mid = (left + right) // 2  # Find the middle index
        if arr[mid] == target:  # Target found
            return mid
        elif arr[mid] < target:  # Target is larger, search right half
            left = mid + 1
        else:  # Target is smaller, search left half
            right = mid - 1

    return -1  # Target not found

# Example
nums = [-1, 0, 3, 5, 9, 12]
print(binary_search(nums, 9))  # Output: 4


# -------------------------------------------------------------
# II. Sorting (Easy) - LeetCode #977 | Squares of a Sorted Array
# -------------------------------------------------------------

# Importance: ⭐⭐⭐⭐☆ (4/5)
# - Good problem to practice Sorting + Two Pointers technique.
# - Practice handling arrays with negative numbers.

# Goal:
# - Return an array of squares of each number, sorted in non-decreasing order.

def sorted_squares(arr):
    left, right = 0, len(arr) - 1  # Two pointers from both ends
    result = [0] * len(arr)  # Result array initialized with zeros
    position = len(arr) - 1  # Position to insert square from the back

    while left <= right:
        if abs(arr[left]) > abs(arr[right]):  # Compare absolute values
            result[position] = arr[left] ** 2  # Square of larger absolute value
            left += 1  # Move left pointer
        else:
            result[position] = arr[right] ** 2  # Square of larger absolute value
            right -= 1  # Move right pointer
        position -= 1  # Move position backward

    return result

# Example
nums = [-4, -1, 0, 3, 10]
print(sorted_squares(nums))  # Output: [0, 1, 9, 16, 100]


# -------------------------------------------------------------
# III. Binary Search (Easy) - LeetCode #35 | Search Insert Position
# -------------------------------------------------------------

# Importance: ⭐⭐⭐⭐☆ (4/5)
# - An application of Binary Search.
# - Find position to insert if the value is not found.

# Goal:
# - Return the index of target in sorted array, or the position to insert it.

def search_insert(arr, target):
    left, right = 0, len(arr) - 1  # Initialize search range

    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        if arr[mid] == target:  # Target found
            return mid
        elif arr[mid] < target:  # Search right half
            left = mid + 1
        else:  # Search left half
            right = mid - 1

    return left  # Return insertion position if not found

# Examples
nums = [1, 3, 5, 6]
print(search_insert(nums, 5))  # Output: 2
print(search_insert(nums, 2))  # Output: 1
print(search_insert(nums, 7))  # Output: 4


# -------------------------------------------------------------
# IV. Binary Search (Easy) - LeetCode #278 | First Bad Version
# -------------------------------------------------------------

# Importance: ⭐⭐⭐⭐⭐ (5/5)
# - A variation of Binary Search, frequently asked.

# Goal:
# - Find the first bad version among n versions.

# Note: `isBadVersion(version)` is a predefined API provided by the problem.

# Example of predefined function for demonstration purposes
def isBadVersion(version):
    BAD_VERSION = 4  # Example bad version
    return version >= BAD_VERSION

def first_bad_version(n):
    left, right = 1, n  # Search range starts from 1 to n
    while left < right:
        mid = (left + right) // 2  # Find the middle version
        if isBadVersion(mid):  # If mid is bad, search left half
            right = mid
        else:  # If mid is good, search right half
            left = mid + 1
    return left  # First bad version

# Example
print(first_bad_version(5))  # Output: 4 (example case)

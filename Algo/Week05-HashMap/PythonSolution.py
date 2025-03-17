# Week 5 Problems: HashMap Applications

# -------------------------------------------------------------
# I. Single Number (LeetCode #136)
# -------------------------------------------------------------

# Importance: ⭐⭐⭐⭐⭐ (5/5)
# - Frequently asked in interviews.
# - Can be solved using HashMap or Bitwise XOR.

# Problem Overview:
# - Given an array of integers, where every element appears twice except for one element.
# - Find the element that appears only once.

# Approach 1 (Using HashMap):
# 1. Use a HashMap (dictionary) to count the frequency of each number.
# 2. Iterate over the HashMap to find the number that appears exactly once.

def singleNumber_hashmap(nums):
    num_count = {}  # Create a HashMap

    for num in nums:
        num_count[num] = num_count.get(num, 0) + 1  # Count occurrences

    for key, value in num_count.items():
        if value == 1:  # Return the number that appears only once
            return key


# Approach 2 (Using Bitwise XOR):
# 1. XOR all the elements.
# 2. Since a ^ a = 0 and 0 ^ b = b, duplicates will cancel out and leave the single number.

def singleNumber_xor(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR operation
    return result


# -------------------------------------------------------------
# II. Intersection of Two Arrays II (LeetCode #350)
# -------------------------------------------------------------

# Importance: ⭐⭐⭐⭐☆ (4/5)
# - HashMap-based intersection problem.
# - Frequently asked in interviews.

# Problem Overview:
# - Given two arrays nums1 and nums2.
# - Find the intersection, including duplicates as many times as they appear in both arrays.

# Approach 1 (Using HashMap):
# 1. Use a HashMap to store the frequency of elements in nums1.
# 2. Iterate through nums2 and for each number:
#    - If the number exists in the HashMap with a count > 0:
#        - Add it to the result list.
#        - Decrement its count in the HashMap.

def intersect_hashmap(nums1, nums2):
    num_count = {}
    result = []

    for num in nums1:
        num_count[num] = num_count.get(num, 0) + 1  # Count frequency

    for num in nums2:
        if num in num_count and num_count[num] > 0:
            result.append(num)
            num_count[num] -= 1  # Reduce count to avoid duplicates

    return result


# Approach 2 (Using Counter):
# 1. Use collections.Counter to count the frequency of nums1.
# 2. Iterate over nums2 and add common elements while reducing counts.

from collections import Counter

def intersect_counter(nums1, nums2):
    counts = Counter(nums1)
    result = []

    for num in nums2:
        if counts[num] > 0:
            result.append(num)
            counts[num] -= 1  # Avoid extra duplicates

    return result


# -------------------------------------------------------------
# III. Valid Anagram (LeetCode #242)
# -------------------------------------------------------------

# Importance: ⭐⭐⭐⭐☆ (4/5)
# - Basic problem using HashMap to compare two strings.
# - Frequently asked in interviews.

# Problem Overview:
# - Given two strings s and t.
# - Check if t is an anagram of s (same letters and same counts).

# Approach 1 (Using HashMap):
# 1. If lengths of s and t are different, return False.
# 2. Count occurrences of each character in s using a HashMap.
# 3. Iterate over t and decrease count for each character.
# 4. If any character is missing or count is zero, return False.
# 5. If all counts match, return True.

def isAnagram_hashmap(s, t):
    if len(s) != len(t):  # If lengths are different, not an anagram
        return False

    char_count = {}

    for char in s:  # Count characters in s
        char_count[char] = char_count.get(char, 0) + 1

    for char in t:  # Subtract counts using t
        if char not in char_count or char_count[char] == 0:
            return False  # Not enough of char in s
        char_count[char] -= 1

    return True  # All characters match


# Approach 2 (Using Counter):
# 1. Use collections.Counter to count characters in both s and t.
# 2. If the counts are equal, they are anagrams.

def isAnagram_counter(s, t):
    return Counter(s) == Counter(t)


# -------------------------------------------------------------
# Example Test Runs
# -------------------------------------------------------------

if __name__ == "__main__":
    # Single Number Examples
    print("Single Number (HashMap):", singleNumber_hashmap([4, 1, 2, 1, 2]))  # Output: 4
    print("Single Number (XOR):", singleNumber_xor([4, 1, 2, 1, 2]))          # Output: 4

    # Intersection of Two Arrays II Examples
    print("Intersection (HashMap):", intersect_hashmap([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [4, 9]
    print("Intersection (Counter):", intersect_counter([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [4, 9]

    # Valid Anagram Examples
    print("Is Anagram (HashMap):", isAnagram_hashmap("anagram", "nagaram"))  # Output: True
    print("Is Anagram (Counter):", isAnagram_counter("anagram", "nagaram"))  # Output: True
    print("Is Anagram (HashMap):", isAnagram_hashmap("rat", "car"))          # Output: False
    print("Is Anagram (Counter):", isAnagram_counter("rat", "car"))          # Output: False

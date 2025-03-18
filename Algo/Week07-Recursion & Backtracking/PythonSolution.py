# Week 7 Problems: Recursion & Backtracking

# -------------------------------------------------------------
# I. Recursion (Easy) - LeetCode #509 | Fibonacci Number
# -------------------------------------------------------------

# Importance: ⭐⭐⭐⭐☆ (4/5)
# - Fundamental problem to understand recursion.
# - Helps analyze performance differences between recursion and iteration.

# Goal:
# - Implement a function to calculate Fibonacci numbers.
# - `F(n) = F(n-1) + F(n-2)`, where `F(0) = 0`, `F(1) = 1`.

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# Example
print(fib(5))  # Output: 5


# -------------------------------------------------------------
# II. Recursion (Easy) - LeetCode #1137 | N-th Tribonacci Number
# -------------------------------------------------------------

# Importance: ⭐⭐⭐⭐☆ (4/5)
# - Extends the Fibonacci concept by summing three previous values.

# Goal:
# - Compute `T(n) = T(n-1) + T(n-2) + T(n-3)`, given base cases:
#   `T(0) = 0`, `T(1) = 1`, `T(2) = 1`.

def tribonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


# Example
print(tribonacci(5))  # Output: 7


# -------------------------------------------------------------
# III. Backtracking (Easy) - LeetCode #784 | Letter Case Permutation
# -------------------------------------------------------------

# Importance: ⭐⭐⭐⭐⭐ (5/5)
# - Key problem to understand backtracking.
# - Demonstrates generating string permutations with case variations.

# Goal:
# - Generate all case variations for a given alphanumeric string.

def letterCasePermutation(s):
    res = []

    def backtrack(index, path):
        if index == len(s):
            res.append(path)
            return

        if s[index].isdigit():
            backtrack(index + 1, path + s[index])
        else:
            backtrack(index + 1, path + s[index].lower())
            backtrack(index + 1, path + s[index].upper())

    backtrack(0, "")
    return res


# Example
print(letterCasePermutation("a1b2"))  # Output: ['a1b2', 'a1B2', 'A1b2', 'A1B2']


# -------------------------------------------------------------
# IV. Backtracking (Easy) - LeetCode #77 | Combinations
# -------------------------------------------------------------

# Importance: ⭐⭐⭐⭐☆ (4/5)
# - Classic problem to practice recursive combination generation.

# Goal:
# - Generate all possible combinations of `k` numbers from `1` to `n`.

def combine(n, k):
    res = []

    def backtrack(start, path):
        if len(path) == k:
            res.append(path[:])
            return

        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()  # Backtracking

    backtrack(1, [])
    return res


# Example
print(combine(4, 2))  # Output: [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]

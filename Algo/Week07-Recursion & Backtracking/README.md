# **Week 7: Recursion & Backtracking**

---

## **1. Recursion**

### **1.1 What is Recursion?**

- A technique where a **function calls itself** to solve a problem
- **Can solve repetitive problems without using loops**

#### **Example: Sum of numbers from 1 to N**

```python
def sum_n(n):
    if n == 1:  # Base Case
        return 1
    return n + sum_n(n - 1)  # Recursive Case

print(sum_n(5))  # Output: 15 (5 + 4 + 3 + 2 + 1)
```

---

### **1.2 Recursion Process (Stack Structure)**

- Recursion uses a **stack structure**
- Function calls follow the **LIFO (Last In First Out) principle**

📌 **Execution process of `sum_n(3)`**

```
sum_n(3) = 3 + sum_n(2)
sum_n(2) = 2 + sum_n(1)
sum_n(1) = 1  (Base Case)
```

✅ **Actual execution order:** `sum_n(1) → sum_n(2) → sum_n(3)`

---

### **1.3 Recursion vs Iteration**

|Method|Advantages|Disadvantages|
|---|---|---|
|**Recursion**|Concise code, suitable for tree traversal|Higher memory usage, risk of infinite loops|
|**Iteration**|Memory efficient, faster|Code may be longer|

---

## **2. DFS (Depth-First Search)**

### **2.1 What is DFS?**

- **An algorithm that visits all nodes in a graph or tree**
- **Explores one path fully before backtracking to explore another path**

📌 **DFS Algorithm Steps**

1. Start from the initial node
2. **Move forward as far as possible in one direction**
3. When no further movement is possible, **backtrack and explore other paths**
4. Repeat until all nodes are visited

---

### **2.2 DFS Execution Process**

📌 **Example Graph**

```
     1
    / \
   2   3
  / \    \
 4   5    6
```

📌 **DFS Traversal Order**

```
1 → 2 → 4 → (Backtrack) → 5 → (Backtrack) → 3 → 6 → (Backtrack)
```

📌 **Graph Representation in Code**

```python
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}
```

---

### **2.3 DFS Implementation Using Recursion**

```python
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)  # Mark node as visited
    print(node, end=" ")  # Print current node
    
    for neighbor in graph[node]:  # Explore child nodes
        dfs(neighbor, visited)

visited = set()
dfs(1, visited)  # Output: 1 2 4 5 3 6
```

---

## **3. Backtracking**

### **3.1 What is Backtracking?**

- **A technique that abandons unpromising paths and backtracks**
- **Based on DFS (Depth-First Search)**
- **More efficient than brute force search**

📌 **Analogy 1: Maze Escape Game**

> "While escaping a maze, if you hit a dead end, you backtrack to find another route."

📌 **Analogy 2: Password Cracking**

> "Instead of trying all combinations from 0000 to 9999, you quickly discard incorrect guesses and find the correct password faster."

---

### **3.2 Core Concepts of Backtracking**

1. **DFS-based exploration**
2. **Pruning → Abandon unpromising paths early**
3. **Recursion → Store current state, make a recursive call, then restore the original state**

---

### **3.3 Backtracking Example: Finding All Permutations**

```python
def backtrack_permutation(nums, path, visited):
    if len(path) == len(nums):  # If all numbers are selected, a permutation is complete
        print("Permutation:", path)
        return

    for i in range(len(nums)):
        if visited[i]:  # Skip already selected numbers
            continue

        visited[i] = True  # Select number
        backtrack_permutation(nums, path + [nums[i]], visited)  # Recursive call
        visited[i] = False  # Backtracking (Undo selection)

nums = [1, 2, 3]
visited = [False] * len(nums)
backtrack_permutation(nums, [], visited)
```

✅ **Using backtracking, all possible cases are explored without repetition!**

---

## **4. Additional Practice Problems**

1. **Finding all subsets (Subsets)**
2. **N-Queens problem (Placing queens without attacking each other)**
3. **Finding a combination of numbers that sums to a target value**

---

## **5. Common Problems Using Backtracking**

|Problem Type|Description|Example Problem|
|---|---|---|
|**Permutation**|Generate all permutations of given numbers|`LeetCode #46`|
|**Combination**|Select a subset of numbers|`LeetCode #77`|
|**Subsets**|Find all possible subsets of a given set|`LeetCode #78`|
|**N-Queens Problem**|Place queens on a chessboard without attacking each other|`LeetCode #51`|
|**Pathfinding (Maze, Sudoku)**|Maze solving, Sudoku solving, etc.|`LeetCode #37`|

---

## **6. Key Takeaways**

1. **Backtracking is a DFS-based search technique that improves efficiency by pruning unpromising paths.**
2. **"Explore all possible solutions but avoid unnecessary exploration."**
3. **Commonly used in permutations, combinations, subsets, N-Queens problems, etc.**
4. **Uses recursion and backtracking (undoing steps) to efficiently find optimal solutions.**
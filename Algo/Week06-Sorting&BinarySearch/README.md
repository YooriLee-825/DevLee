# Week 6: Sorting & Binary Search

---

## 1. Sorting

### 1) What is Sorting?

- Arranging multiple pieces of data in a **specific order**.
- Two main orders:
    - **Ascending**: Smallest to largest
    - **Descending**: Largest to smallest

---

### 2) Why Do We Need Sorting?

- To **find things quickly** (especially used with binary search)
- To easily find **maximum and minimum values**
- To **organize data neatly**

---

### 3) Python's Built-in Sorting Functions

- `sorted(list)` → Returns a new sorted list
- `list.sort()` → Sorts the list in place (memory-efficient)

---

### 4) **Common Sorting Algorithms**

#### (1) Bubble Sort

- **Compares two adjacent numbers** and pushes the larger one to the back.
- Called **Bubble Sort** because the largest number "bubbles" up to the end in each pass.
- **Time complexity**: O(n²) (inefficient but good for understanding the concept).

##### Example:

```
Initial: [5, 3, 8, 1]
Pass 1: [3, 5, 1, 8]
Pass 2: [3, 1, 5, 8]
Pass 3: [1, 3, 5, 8] (Done)
```

##### Code:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numbers = [5, 3, 8, 1]
bubble_sort(numbers)
print(numbers)  # [1, 3, 5, 8]
```

---

#### (2) Selection Sort

- **Finds the smallest number** each time and moves it to the front.
- **Time complexity**: O(n²) (inefficient but good for learning).

##### Example:

```
Initial: [5, 3, 8, 1]
Pass 1: [1, 3, 8, 5]
Pass 2: [1, 3, 8, 5]
Pass 3: [1, 3, 5, 8] (Done)
```

##### Code:

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

numbers = [5, 3, 8, 1]
selection_sort(numbers)
print(numbers)  # [1, 3, 5, 8]
```

---

#### (3) Insertion Sort

- Goes through data **one by one from the start**, inserting each in the right place.
- Similar to how people sort cards.
- **Time complexity**: O(n²) (faster if data is already mostly sorted).

##### Example:

```
Initial: [5, 3, 8, 1]
Pass 1: [3, 5, 8, 1]
Pass 2: [3, 5, 8, 1]
Pass 3: [1, 3, 5, 8] (Done)
```

##### Code:

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

numbers = [5, 3, 8, 1]
insertion_sort(numbers)
print(numbers)  # [1, 3, 5, 8]
```

---

### 5) **Comparison of Sorting Algorithms**

|Sorting Method|Principle|Time Complexity (Worst)|Space Complexity|
|---|---|---|---|
|Bubble Sort|Compare adjacent numbers, push larger to back|O(n²)|O(1)|
|Selection Sort|Find smallest and move to front|O(n²)|O(1)|
|Insertion Sort|Insert into proper place|O(n²)|O(1)|
|Python `sorted`|Fast built-in function|O(n log n)|O(n)|

---

## 2. Binary Search

### 1) What is Binary Search?

- A fast way to find a **specific value** in a **sorted list**.
- Cuts the list in half each time to search.
- **Time complexity**: O(log n)

---

### 2) How It Works

#### (Example Data)

```
[1, 3, 5, 8, 10, 14, 18]
```

#### (Searching for: 10)

|Step|Remaining Data|Middle Value|Comparison|Next Range|
|---|---|---|---|---|
|1|[1, 3, 5, 8, 10, 14, 18]|8|8 < 10 (go right)|[10, 14, 18]|
|2|[10, 14, 18]|14|14 > 10 (go left)|[10]|
|3|[10]|10|Found!|End|

---

### 3) Example

```
Start: [1, 3, 5, 8, 10, 14, 18]  -> Mid: 8 (go right)
Next:                [10, 14, 18] -> Mid: 14 (go left)
Last:             [10] -> Found!
```

---

### 4) Code Example

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return index
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Not found

numbers = [1, 3, 5, 8, 10, 14, 18]
print(binary_search(numbers, 10))  # Output: 4
```
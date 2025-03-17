# **Week 5: HashMap Basics and Applications**

---

## **1. What is a HashMap?**

- A **HashMap** is a data structure that stores **Key-Value pairs**.
- You can **quickly find, insert, and delete** data.  
  → **Time complexity**: O(1) for most operations.
- In Python, a HashMap is called a **`dict` (dictionary)**.

---

## **2. Why Do We Use HashMap?**

- To **find data fast** (list takes O(N), but HashMap takes O(1)).
- To **avoid duplicates** and **count** how many times data appears.
- To **map keys to values quickly** for tasks like **caching, counting, and grouping**.

---

## **3. HashMap vs. Other Data Structures**

| Data Structure       | Description                                | Average Lookup Time |
| -------------------- | ------------------------------------------ | ------------------- |
| **HashMap (`dict`)** | Stores Key-Value pairs, fast search        | **O(1)**            |
| **List (`list`)**    | Stores data in order, slow search          | O(N)                |
| **Set (`set`)**      | Stores unique items, fast membership check | **O(1)**            |

---

## **4. Basic Usage of HashMap (`dict`)**

### **Creating and Using HashMap**

```python
# Create
hash_map = {}

# Insert
hash_map["apple"] = 5
hash_map["banana"] = 10

# Retrieve
print(hash_map["apple"])  # Output: 5

# Update
hash_map["apple"] = 7

# Delete
del hash_map["banana"]

# Check if key exists
if "apple" in hash_map:
    print("Key exists")
```

---

### **Get All Keys, Values, and Items**

```python
hash_map = {"apple": 5, "banana": 10, "cherry": 15}

print(hash_map.keys())   # dict_keys(['apple', 'banana', 'cherry'])
print(hash_map.values()) # dict_values([5, 10, 15])
print(hash_map.items())  # dict_items([('apple', 5), ('banana', 10), ('cherry', 15)])
```

---

## **5. `defaultdict`: HashMap with Default Values**

### **Problem with Regular `dict`**

```python
hash_map = {}
print(hash_map["apple"])  # KeyError (if key doesn't exist)
```

---

### **Using `defaultdict` to Avoid Errors**

```python
from collections import defaultdict

# Create with default value 0
hash_map = defaultdict(int)

hash_map["apple"] += 1
print(hash_map["apple"])  # Output: 1
print(hash_map["banana"])  # Output: 0 (default value)
```

---

### **Using `defaultdict` with List**

```python
hash_map = defaultdict(list)

hash_map["fruits"].append("apple")
hash_map["fruits"].append("banana")

print(hash_map["fruits"])      # ['apple', 'banana']
print(hash_map["vegetables"])  # [] (empty list by default)
```

---

## **6. `Counter`: Easy Way to Count Elements**

### **Count Numbers**

```python
from collections import Counter

nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
count = Counter(nums)

print(count)    # Counter({4: 4, 3: 3, 2: 2, 1: 1})
print(count[3]) # 3
print(count[5]) # 0 (returns 0 if not found)
```

---

### **Count Characters in a String**

```python
text = "hello world"
char_count = Counter(text)

print(char_count)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

---

### **Find Most Common Elements**

```python
words = ["apple", "banana", "apple", "orange", "banana", "banana"]
count = Counter(words)

print(count.most_common(2))  # [('banana', 3), ('apple', 2)]
```

---

## **7. Real Example: Find Intersection of Two Arrays**

### **Problem**

- Find common elements in two lists.

### **Solution Steps**

1. Count frequency of the first list.
2. Check each element of the second list.
3. If it exists in both, add to result and reduce the count to avoid duplicates.

---

### **Code**

```python
from collections import Counter

def intersection(nums1, nums2):
    count = Counter(nums1)
    res = []

    for num in nums2:
        if count[num] > 0:
            res.append(num)
            count[num] -= 1

    return res

print(intersection([1, 2, 2, 1], [2, 2]))  # [2, 2]
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))  # [9, 4]
```

---

### **Time Complexity**

- `Counter(nums1)`: O(N)
- Loop through `nums2`: O(M)
- **Total**: O(N + M)

---

## **8. HashMap Time Complexity Summary**

| Operation                       | Average Time Complexity |
| ------------------------------- | ----------------------- |
| **Insert** (`map[key] = value`) | **O(1)**                |
| **Lookup** (`map[key]`)         | **O(1)**                |
| **Delete** (`del map[key]`)     | **O(1)**                |
| **Loop over all elements**      | **O(N)**                |

---

## **9. Conclusion**

1. **HashMap (`dict`) is very fast** for searching, adding, and deleting data.
2. **`defaultdict` helps avoid errors** by giving default values automatically.
3. **`Counter` makes counting elements easy** and fast.
4. HashMaps are **very important in coding tests and interviews**, so you must practice them well!

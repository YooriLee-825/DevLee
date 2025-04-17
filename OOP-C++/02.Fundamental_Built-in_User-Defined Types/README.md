# **C++ Foundations: Fundamental, Built-in, and User-Defined Types**

## **Introduction**

- C++ offers a variety of **type systems** that form the foundation of programming in C++.
- These include **Fundamental Types**, **Built-in Types (Pointers, References, Arrays)**, and **User-Defined Types (Classes, Structs, Unions, Enumerations)**.
- Understanding these types is essential for building efficient, reusable, and maintainable programs.

---

## **1. Fundamental Types**

### **1.1 Integer Types**

- Store whole numbers.
- **Signed types**: Can hold negative and positive values.
- **Unsigned types**: Only non-negative values.

**Examples:**

```cpp
int a = 91;       // Decimal
int b = 0133;     // Octal
int c = 0x5b;     // Hexadecimal
long int d = 91L; // Long integer
unsigned int e = 91U; // Unsigned integer
```

---

### **1.2 Boolean Type**

- Represents `true` or `false`.

```cpp
bool isStudent = true;
```

---

### **1.3 Character Types**

- Store single characters.
- Types: `char`, `signed char`, `unsigned char`, `wchar_t`, `char16_t`, `char32_t`.

```cpp
char c = 'A';
wchar_t wc = L'A';
char16_t c16 = u'A';
char32_t c32 = U'A';
```

---

### **1.4 Floating-Point Types**

- Store real numbers.
- Types: `float`, `double`, `long double`.

```cpp
float f = 3.14f;
double d = 2.71828;
long double ld = 1.618L;
```

---

### **1.5 `void` Type**

- Represents an empty type.
- Used for functions without a return value and generic pointers.

---

### **1.6 Initialization and Type Inference**

```cpp
int n1 = 7;   // C-style initialization
int n2 {8};   // Brace initialization
auto x = 10;  // Type inference (int)
```

---

### **1.7 Type Alignment**

```cpp
alignof(int); // Check alignment requirement
alignas(16) struct B { int x; };
```

---

## **2. Built-in Types: Pointers, References, Arrays**

### **2.1 Pointers**

- Store memory addresses.

```cpp
int* p = nullptr; // Pointer to int
```

---

### **2.2 Generic Pointers (`void*`)**

- Pointers without specific type information.

```cpp
int num;
void* ptr = &num;
int* p = static_cast<int*>(ptr);
```

---

### **2.3 References**

- **lvalue reference (&)**: Refers to an existing object.
- **rvalue reference (&&)**: Refers to a temporary object.

```cpp
int a = 10;
int& ref = a;  // lvalue reference
int&& temp = 20; // rvalue reference
```

---

### **2.4 Arrays**

- Fixed-size sequence of elements.

```cpp
int arr[5] = {1, 2, 3, 4, 5};
int* dynamicArr = new int[5]; // Heap array
delete[] dynamicArr;
```

---

### **2.5 Aggregate Initialization**

```cpp
int a[] = {1, 2, 3};
int b[5] = {1, 2, 3}; // Remaining elements set to 0
```

---

### **2.6 Range-Based for Loop**

```cpp
int nums[] = {1, 2, 3};
for (int x : nums) std::cout << x << ' ';
```

---

## **3. User-Defined Types: Classes, Structs, Unions, Enumerations**

### **3.1 Classes**

- Encapsulate data and functions.

```cpp
class Item {
    int id;
    std::string name;
public:
    Item(int i, const std::string& n);
    void display() const;
};
```

---

### **3.2 Data Member Initialization**

```cpp
class Product {
    int id = 0;
    std::string name {"None"};
public:
    Product(int i, const std::string& n);
};
```

---

### **3.3 Copy and Move Semantics**

```cpp
class Array {
    int* data;
    unsigned size;
public:
    Array(unsigned s);
    Array(const Array& other);
    Array& operator=(const Array& other);
    Array(Array&& other);
    Array& operator=(Array&& other);
    ~Array();
};
```

---

### **3.4 Anonymous Classes**

```cpp
struct { char shortName[7]; char fullName[41]; } name;
```

---

### **3.5 Static Members and Functions**

```cpp
class Car {
    static unsigned count;
public:
    static unsigned getCount();
};
```

---

### **3.6 Structs and Unions**

- **Structs**: Like classes but default access is `public`.
- **Unions**: Share memory among members.

```cpp
struct Product { int id; char name[50]; };
union Data { int intVal; char charVal[4]; };
```

---

### **3.7 Enumerations**

#### **Plain Enumeration**

```cpp
enum Colour { white, red, green, blue };
```

#### **Scoped Enumeration**

```cpp
enum class Colour { white, red, green, blue };
```

#### **Scoped Enumeration with Underlying Type**

```cpp
enum class Permissions : unsigned char { read = 0x1, write = 0x2, execute = 0x4 };
```

---

## **Summary of Key Concepts**

| Concept               | Description                                         |
| --------------------- | --------------------------------------------------- |
| **Fundamental Types** | Basic types like int, char, float, bool, void       |
| **Pointers**          | Store addresses, support dynamic memory             |
| **References**        | lvalue/rvalue references for flexible access        |
| **Arrays**            | Fixed-size collections of same type elements        |
| **Classes**           | Encapsulate data and functions for OOP              |
| **Structs & Unions**  | Data structures for grouping or sharing memory      |
| **Enumerations**      | Symbolic constants, with optional scoping and types |

---
